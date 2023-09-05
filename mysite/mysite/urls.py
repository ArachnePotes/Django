from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from myapp.views import index,contact,services,info

urlpatterns = [
    path('',index,name='index'),
    path("admin/", admin.site.urls),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('info/',info,name='info'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
