from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class MyUser(AbstractUser):
    user_nickname = models.CharField(max_length=30)
    user_photo = models.ImageField(upload_to="images", default='images/santa.png', blank=True)
    user_intro = models.TextField(blank=True)

    # 좋아요 객체
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following') # 내가 팔로잉하는

    # 유저가 북마크한 포스팅
    bookmark = models.ManyToManyField('post.Post')

# Create your models here.
# class User(models.Model):
#     user_id = models.CharField(max_length = 20)
#     user_password = models.CharField(max_length = 20)
#     user_nickname = models.CharField(max_length=30)
#
#     class Meta:
#         db_table = 'user_table'
