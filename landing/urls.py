


from django.urls import path,  re_path
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from django.contrib import admin

from django.contrib.auth import views as auth_views
app_name = 'app'

urlpatterns = [
    path('', views.app_root, name='app_root'),

]