from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]