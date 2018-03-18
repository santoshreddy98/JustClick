from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts.views import home

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^',include('accounts.urls')),
    url(r'^$',home,name='home'),
]
