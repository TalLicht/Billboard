from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^Billboard_site/', include('Billboard_site.urls')),
    url(r'^admin/', admin.site.urls),
]