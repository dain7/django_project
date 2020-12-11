from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    # 초대되지 않은 유저는 못보게함
    # path('unauthorized/', views.authorized, name='unauthorized'),
    # path('<str:group_id>/', views.room, name='room'),
]
