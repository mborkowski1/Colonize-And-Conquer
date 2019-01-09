from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_your_alliance, name='show_your_alliance'),
    path('<int:id_of_user>', views.user_your_alliance_detail_page, name='user_your_alliance_detail_page'),
    path('forum/<int:id_of_alliance>', views.show_alliance_forum, name='show_alliance_forum'),
    path('edycjaSojuszu/', views.edit_your_alliance, name='edit_your_alliance'),
    path('zaprosDoSojuszu/', views.invite_to_your_alliance, name='invite_to_your_alliance'),
    path('listOfAlliances/', views.alliance_list_page, name='alliance_list_page'),
    path('listOfAlliances/<int:id_of_alliance>/', views.alliance_detail_page, name='alliance_detail_page'),
    path('listOfAlliances/<int:id_of_alliance>/<int:id_of_user>', views.user_detail_page, name='user_detail_page'),
    path('forum/<int:id_of_alliance>/postForum', views.add_forum_post, name='add_forum_post'),
    path('forum/<int:id_of_alliance>/topic', views.add_forum_topic, name='add_forum_topic'),
    path('forum/<int:id_of_alliance>/subForum', views.add_forum_sub_forum, name='add_forum_sub_forum'),
]
