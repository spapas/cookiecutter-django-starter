from django.conf import settings
from django.conf.urls import url, include 
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    
    url(r'^login/$', login, name='auth_login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='auth_logout'),

]
