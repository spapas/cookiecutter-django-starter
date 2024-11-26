from django.views.generic import FormView
from typing import Any
from django import forms
from django.contrib.auth import get_user_model
+
+
class HijackForm(forms.Form):
    username = forms.CharField()


class HijackFormView(FormView):
    template_name = "hijack.html"
    form_class = HijackForm

    def get_context_data(self, **kwargs):
        User = get_user_model()
        ctx = super().get_context_data(**kwargs)

        ctx["user"] = User.objects.get(username=self.request.GET.get("username"))
        return ctx
