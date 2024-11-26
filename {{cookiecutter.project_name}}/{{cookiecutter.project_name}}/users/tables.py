import django_tables2 as tables
from django_tables2_column_shifter.tables import ColumnShiftTableBootstrap5
from . import models
from django.utils.html import mark_safe
from django_tables2.utils import A


class UserTable(ColumnShiftTableBootstrap5):
    #id = tables.LinkColumn(
    #    "app_detail",
    #   args=[A("id")],
    #    verbose_name="ΚΩΔ",
    #    attrs={"a": {"class": "btn btn-primary btn-sm"}},
    #)

    id = tables.TemplateColumn("""
        <a href="{% url 'hijack-action' %}?username={{ record.username }}" class="btn btn-danger btn-sm">{{ record.id }}</a>
    """, verbose_name="Hijack")

    
    class Meta:
        model = models.User
        fields = ("id", "username", "last_name", "first_name", "last_login")
        attrs = {"class": "table table-sm table-stripped"}
        empty_text = "No entries"
