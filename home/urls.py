from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('purchase_request', views.purchase_request, name='purchase_request'),
]
