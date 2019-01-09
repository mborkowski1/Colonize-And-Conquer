from django.urls import path
from . import views

urlpatterns = [
    path('podgladProfil/', views.profile_page, name='profile_page'),
    path('', views.profilowe_page, name='profilowe_page'),
]
