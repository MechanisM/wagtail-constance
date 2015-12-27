Wagtail-Constance
~~~~~~~~~~~~~~~~~

I know there is `wagtail.contrib.settings` available, but I'm so much love django-constance with redis backend!



Installation
------------

Make sure you installed `django-constance <https://github.com/jazzband/django-constance>`_ then install wagtail-constance:

.. code-block:: sh
    
    pip install wagtail-constance


And then just add `wagtailconstance` into `INSTALLED_APPS`:

.. code-block:: py

    INSTALLED_APPS = (
       ...
       'wagtailconstance',
       ...
    )

Note
----

I'm not added wagtail or constance as requirements in setup.py.
I'm tested it out only with python 3.5.1


Credits
-------

* Released under `MIT License <http://www.opensource.org/licenses/mit-license.php>`_
* `wagtail <https://github.com/torchbox/wagtail>`_
* `django-constance <https://github.com/jazzband/django-constance>`_
* this `snippet <https://djangosnippets.org/snippets/10462/>`_