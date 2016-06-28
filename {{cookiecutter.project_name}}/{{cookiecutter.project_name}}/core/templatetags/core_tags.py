from django import template
from django.conf import settings
from django.template import Context

register = template.Library()

@register.simple_tag
def get_setting_value(value):
    return getattr(settings, value)

