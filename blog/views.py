from django.shortcuts import render, redirect
from post.models import Post, Reply
from member.models import MyUser

from itertools import chain
# Create your views here.

def main(request):
    if request.method == 'GET':
        if request.session.get('username'): # 세션에 값이 있으면
            user_id = request.session.get('username')
            user = MyUser.objects.get(username=user_id)
            # post = Post.objects.all() # 포스팅 출력

            following = user.following.all() # 내 팔로워 리스트
            following = chain(following, [request.user]) # 내가 쓴 글 포함

            post = Post.objects.filter(posting_writer__in = following).order_by('-posting_date')
            return render(request, 'blog/main.html', {'post': post, 'user':user, })
        else:
            return redirect('/accounts/login/')
