from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_setting_value(value):
    return getattr(settings, value)


@register.simple_tag
def get_template_file(view):

    import os

    from django import template

    if view.template_name:
        template_name = view.template_name
    else:
        template_name = "".join(view.get_template_names())

    for engine in template.engines.all():
        for loader in engine.engine.template_loaders:
            for origin in loader.get_template_sources(template_name):
                if os.path.exists(origin.name):
                    return origin.name


def get_cls_file(cls):
    import inspect

    filepath = inspect.getfile(cls)
    try:
        lineno = inspect.getsourcelines(cls)[1]
    except OSError:
        return None
    return f"{filepath}:{lineno}"


@register.simple_tag
def get_view_file(view):
    return get_cls_file(view.__class__)

    # filepath = inspect.getfile(view.__class__)
    # lineno = inspect.getsourcelines(view.__class__)[1]
    # return f"{filepath}:{lineno}"


@register.simple_tag(takes_context=True)
def other_context_vars(context):
    from django.db.models import Model, QuerySet
    from django.forms import BaseForm
    from django.utils.html import format_html
    from django_filters import FilterSet
    from django_tables2 import Table

    cok = {}
    for k, v in context.flatten().items():
        if isinstance(v, Model):
            cok[k] = format_html(
                f"<a href='vscode://file/{get_cls_file(v.__class__)}'>{v.__class__.__name__}</a> ({v.id})"
            )

        elif isinstance(v, QuerySet):
            vv = v.first()
            if vv:
                cok[k] = format_html(
                    f"<a href='vscode://file/{get_cls_file(v.model)}'>{v.model.__name__}</a> ({vv.id}, ...)"
                )

        elif isinstance(v, Table | FilterSet | BaseForm):

            cok[k] = format_html(
                f"<a href='vscode://file/{get_cls_file(v.__class__)}'>{v.__class__.__name__}</a>"
            )
        elif k == "inlines":
            cok[k] = str(v)

    return cok

