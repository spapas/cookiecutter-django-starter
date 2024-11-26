from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import HijackFormView


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("login/", LoginView.as_view(), name="auth_login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="auth_logout"),
    path("hijack-action/", user_passes_test(lambda u: u.is_superuser is True)(HijackFormView.as_view()), name="hijack-action"),
]
