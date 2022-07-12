from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cluster/', views.cluster_data, name='clusters'),
]