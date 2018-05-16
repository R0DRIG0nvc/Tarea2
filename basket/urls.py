from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.list, name="player_list"),
    path('add', views.add, name="player_add"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
]
