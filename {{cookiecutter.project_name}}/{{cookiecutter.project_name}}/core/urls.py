from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import permission_required
from .views import hijack_form, hijack_action


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("login/", LoginView.as_view(), name="auth_login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="auth_logout"),
        path(
        "hijack-form/",
        permission_required("hijack.permissions.superusers_only")(hijack_form),
        name="hijack-form",
    ),
    path(
        "hijack-action/",
        permission_required("hijack.permissions.superusers_only")(hijack_action),
        name="hijack-action",
    ),
]
