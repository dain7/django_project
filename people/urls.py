from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.profile, name='profile'), # 프로필 들어가기
    path('edit/<int:id>', views.profile_edit, name='profile_edit'), # 프로필 수정

    # 팔로우
    path('follow/<follow_id>', views.follow, name="follow"), # 팔로우
    path('follow_list/<id>', views.follow_list, name="follow_list"), # 팔로워 리스트
    path('following_list/<id>', views.following_list, name="following_list"),
    path('list_follow/<follow_id>', views.list_follow, name="list_follow"), # 리스트에서 팔로우 기능

    # 저장된 게시물
    path('<int:id>/saved/', views.saved_posting, name='saved')
]
