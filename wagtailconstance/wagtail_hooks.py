from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from .views import ConstanceConfigView
from django.urls import include, re_path


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^config/', ConstanceConfigView.as_view(), name='constance_config'),
    ]


class ConstanceMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register('register_settings_menu_item')
def register_constance_menu_item():
    return ConstanceMenuItem(_('Constance config'), reverse('constance_config'), classnames='icon icon-cogs', order=800)
