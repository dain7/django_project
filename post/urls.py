from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.create, name='create'),

    # 게시글 주요기능
    path('', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'), # 포스팅 자세히 보기

    #댓글 주요가능
    path('reply/<int:id>', views.reply_create, name='reply_create'), # 댓글 생성 - 메인페이지
    path('dtreply/<int:id>', views.comment_create, name='comment_create'), # 댓글 생성 - 페이지 자세히보기
    path('reply_delete/<int:p_id>/<int:r_id>', views.comment_delete, name="comment_delete"), # 댓삭

    #게시글 부가기능

    path('like/', views.post_like, name="post_like"),  # 좋아요
    path('search/<tag>/', views.search, name="search"),  # 검색
    path('bookmark/', views.bookmark, name="bookmark"), # 북마크
]
