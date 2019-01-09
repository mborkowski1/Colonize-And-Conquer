from django.urls import path
from . import views

urlpatterns = [
    path('kontakt/', views.kontakt, name='kontakt'),
    path('cookies/', views.cookies, name='cookies'),
    path('zasady/', views.zasady, name='zasady'),
]