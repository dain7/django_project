from django.db import models
from member.models import MyUser
from post.models import Post
# Create your models here.


# class Follow(models.Model):
#     user = models.ForeignKey(MyUser, unique=True, on_delete=models.CASCADE)
#
#     following = models.ManyToManyField(MyUser, default=0, related_name="following")
#     follower = models.ManyToManyField(MyUser, default=0, related_name="follower")
