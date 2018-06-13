from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('list',views.List.as_view(), name = 'list'),
]