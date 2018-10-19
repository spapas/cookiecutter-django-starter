from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="home.html"), name="home"),
    url(r"^login/$", LoginView.as_view(), name="auth_login"),
    url(r"^logout/$", LogoutView.as_view(), {"template_name": "logout.html"}, name="auth_logout"),
]
