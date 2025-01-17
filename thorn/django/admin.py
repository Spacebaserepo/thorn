"""Django-Admin interface support

Adds support for managing webhook subscriptions in the Django admin.
"""


from django.contrib import admin

from . import models

admin.site.register(models.Subscriber)
