from django.urls import path
from messagess import views

urlpatterns = [
    path('', views.messages_page, name='messages_page'),
    path('wyslane/', views.messages_your_send_page, name='messages_your_send_page'),
    path('napisz/', views.messages_send_page, name='messages_send_page'),
    path('<int:id_of_message>/', views.messages_detail_page, name='messages_detail_page'),
]
