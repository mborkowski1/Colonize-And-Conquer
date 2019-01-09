from django.urls import path
from . import views

urlpatterns = [
    path('dodajSurowce/', views.dodaj_surowce, name='dodaj_surowce'),
    path('zaktualizujAtaki/', views.zaktualizuj_ataki, name='zaktualizuj_ataki'),
    path('zaktualizujWsparcie/', views.zaktualizuj_wsparcie, name='zaktualizuj_wsparcie'),
]
