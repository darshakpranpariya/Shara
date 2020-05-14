from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('addtips/', views.addtips, name='addtips'),
    path('logout/', views.logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
