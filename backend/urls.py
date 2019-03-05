from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin

from notes import endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(endpoints)),
    url(r'^api/auth/', include('knox.urls'))
]