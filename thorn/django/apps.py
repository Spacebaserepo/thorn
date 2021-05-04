"""Thorn Django application configurations."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

__all__ = ['WebhooksConfig']


class WebhooksConfig(AppConfig):
    name = 'thorn.django'
    label = 'webhooks'
    verbose_name = _('Webhooks')
