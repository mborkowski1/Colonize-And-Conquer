from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_map, name='main_page_map'),
    path('<int:id_of_city>/', views.city_detail_info, name='city_detail_info'),
    path('<int:id_of_city>/atak/', views.city_attack, name='city_attack'),
    path('<int:id_of_city>/wsparcie/', views.city_support, name='city_support'),
    path('<int:id_of_city>/<int:id_of_user>/', views.city_owner_detail_info, name='city_owner_detail_info'),
]
