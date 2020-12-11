from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Post, Reply, Tag
from member.models import MyUser
from .form import PostForm
import json
from django.views.decorators.http import require_GET, require_POST
import re

# Create your views here.



# 게시글 주요 기능
# 게시글 쓰기
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            user = MyUser.objects.get(id=request.user.id)
            post = form.save(commit=False)
            post.posting_writer = user
            post.save()

            # 태그처리
            content = request.POST.get('posting_content')
            tags = re.findall(r'#(\w+)\b', content)

            for c in tags:
                tag = Tag()
                tag.tag_content = c
                tag.save()
                post.tagging.add(tag)


            return redirect('/')
        else:
            return redirect('create')

    elif request.method == "GET":
        form = PostForm()
        return render(request, 'post/create.html', {'form':form})

# 게시글 수정
def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.photing_photo = request.FILES.get('posting_photo')
        post.posting_content = request.POST['posting_content']

        # 태그 수정
        tags = post.tagging.all().delete() # 기존 태그 삭제

        content = request.POST['posting_content'] # 수정 내용 가져오기
        tags = re.findall(r'#(\w+)\b', content) # 태그 추출

        for c in tags:
            tag = Tag()
            tag.tag_content = c
            tag.save()

            post.tagging.add(tag)

        post.save()
        return redirect('/')
    else:
        form = PostForm(instance=post)
        return render(request, 'post/edit.html', {'form':form})

# 게시글 삭제
def delete(request, id):
    post = Post.objects.get(id=id)
    tags = post.tagging.all() # 연관된 태그 삭제
    tags.delete()
    post.delete()

    return redirect('/')

# 게시글 자세히 보기
def detail(request, id):
    user_id = request.session['username']
    user = MyUser.objects.get(username=user_id)
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        reply = Reply.objects.filter(posting_id=id)
        return render(request, 'post/post_detail.html', {'post':post, 'reply':reply, 'user':user})


# 댓글 기능 (메인)
def reply_create(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        reply = Reply(posting_id=post)
        # reply = Reply()
        reply.reply_content = request.POST['reply']
        reply.reply_writer = request.session.get('username')
        reply.save()
    return redirect('/')


# 댓글 기능 (디테일)
def comment_create(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        reply = Reply(posting_id=post)
        reply.reply_content = request.POST['reply']
        reply.reply_writer = request.session.get('username')
        reply.save()
        return redirect('detail', id)


# 댓글 삭제
def comment_delete(request, p_id, r_id):
        reply = Reply.objects.get(id=r_id)
        reply.delete()
        return redirect('detail', p_id)




# 게시글 부가기능
# 게시글 좋아요 (메인페이지)
@require_POST
def post_like(request):

    if request.is_ajax():
        id = request.POST.get('blog_id') #templates로부터 blog_id를 입력받음
        post = Post.objects.get(id=id)

        user = request.user

        if post.like_user.filter(id=user.id).exists(): # 이미 좋아요를 누른 유저
            post.like_user.remove(user)
            post.save()
            message = "좋아요 취소!"
        else:
            post.like_user.add(user)
            post.save()
            message = "좋아요!"

        context = {'like_count': post.like_user.count(), "message" : message}
        return HttpResponse(json.dumps(context), content_type='application/json')

# 태그 및 키워드 검색 기능
def search(request, tag=None):
    if request.method=='GET':
        keyword = tag
    else:
        keyword = request.POST.get('search_button')

    tag = Tag.objects.filter(tag_content=keyword)
    post = Post.objects.filter(tagging__in = tag).order_by('-posting_date')

    if post:
        post_ = post[0]
    else:
        post_ = None

    return render(request, 'post/search_result.html', {'post':post, 'keyword':keyword, 'post_':post_})

# 북마크 기능
def bookmark(request):
    if request.is_ajax():
        id = request.POST.get('posting_id')
        user = request.user
        post = Post.objects.get(pk=id)

        if user.bookmark.filter(pk=id).exists():
            user.bookmark.remove(post)
            message = '북마크 취소'
        else:
            user.bookmark.add(post)
            message = '북마크'
        print('message')
        context = {"message" : message}
        return HttpResponse(json.dumps(context), content_type='application/json')
