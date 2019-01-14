from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'premium'

urlpatterns = [
    path('', views.premium_page, name='premium_page'),
    path('platnosc/', views.premium_platnosc, name='premium_platnosc'),
    path('historia/', views.premium_history, name='premium_history'),
    path('platnosc/<int:typPremium>/', views.payment_process, name='process'),
    path('platnosc/<int:payment_id>/done/', views.payment_done, name='done'),
    path('platnosc/<int:payment_id>/canceled/', views.payment_canceled, name='canceled'),
]
