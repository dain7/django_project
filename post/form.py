from django import forms
from .models import Post, Reply


# 글쓰기 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['posting_photo', 'posting_content']



# 댓글쓰기 폼
# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model = Reply
#         fields = ['reply_content']
