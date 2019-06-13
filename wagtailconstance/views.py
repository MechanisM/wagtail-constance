from operator import itemgetter
from django.urls import reverse_lazy
from django.utils.formats import localize
from django.views.generic.edit import FormView
from django.utils.translation import ugettext_lazy as _
from wagtail.admin import messages

from constance import settings, LazyConfig
from constance.admin import ConstanceForm

config = LazyConfig()


class ConstanceConfigView(FormView):
    form_class = ConstanceForm
    template_name = "wagtailconstance/config.html"
    success_url = reverse_lazy("constance_config")

    def __init__(self, *args, **kwargs):
        if "fields" in kwargs:
            self.fields = kwargs.pop("fields")
        else:
            self.fields = settings.CONFIG.keys()
        super(ConstanceConfigView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ConstanceConfigView, self).get_context_data(**kwargs)
        context["config"] = []
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        initial = self.get_initial()
        # for name, (default, help_text) in settings.CONFIG.items():
        for name, field_data in settings.CONFIG.items():
            default = field_data[0]
            help_text = field_data[1] if len(field_data) > 1 else ""
            value = initial.get(name)
            if value is None:
                value = getattr(config, name)
            context["config"].append(
                {
                    "name": name,
                    "default": localize(default),
                    "help_text": _(help_text),
                    "value": localize(value),
                    "modified": value != default,
                    "form_field": form[name],
                }
            )
        context["config"].sort(key=itemgetter("name"))
        return context

    def get_initial(self):
        data = super(ConstanceConfigView, self).get_initial()
        default_initial = (
            (name[0], name[1])
            for name in settings.CONFIG.items()
            if name in self.fields
        )
        initial = dict(
            default_initial,
            **dict(
                config._backend.mget(
                    [k for k in settings.CONFIG.keys() if k in self.fields]
                )
            )
        )
        data.update(initial)
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("Live settings updated successfully."))
        return super(ConstanceConfigView, self).form_valid(form)
