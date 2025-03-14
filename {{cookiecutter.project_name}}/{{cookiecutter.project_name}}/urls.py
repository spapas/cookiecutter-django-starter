"""
{{cookiecutter.project_name}} URL Configuration
"""
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("", include("{{cookiecutter.project_name}}.core.urls")),
    path("users/", include("{{cookiecutter.project_name}}.users.urls")),
    path("hijack/", include("hijack.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
    except:
        pass
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

