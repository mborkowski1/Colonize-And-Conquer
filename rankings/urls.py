from django.urls import path
from . import views

urlpatterns = [
    path('', views.ranking_page, name='ranking_page'),
    path('<int:id_of_user>/', views.user_detail_info, name='user_detail_info'),
    path('<int:id_of_user>/<int:id_of_city>/', views.user_city_detail_info, name='user_city_detail_info'),
]
