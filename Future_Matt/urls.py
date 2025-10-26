from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.views.generic import RedirectView

import django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # Serve favicon at /favicon.ico by redirecting to the static file path
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'Portfolio/images/favicon/matt-kerby-logo.ico')),

]

if settings.DEBUG:
        urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
