from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('fillTablePos/', views.fill_village_pos_table, name='fill_village_pos_table'),
    path('thingsStats/', views.generate_basic_tables, name='generate_basic_tables'),
    path('<int:id_of_article>/', views.show_article_details, name='show_article_details'),
    path('forum/', views.show_forum, name='show_forum'),
    path('faq/', views.show_faq, name='show_faq'),
    path('support/', views.show_support, name='show_support'),
]
