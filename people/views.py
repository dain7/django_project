from django.shortcuts import render, redirect
from member.models import MyUser
from post.models import Post
from .form import ProfileEditForm
from django.shortcuts import get_object_or_404
# Create your views here.

# 프로필 페이지
def profile(request, id):
    if request.method == 'GET':
        user = MyUser.objects.get(pk=id) # user 객체 오픈
        # profile = Profile(user=user) # 프로필 객체 오픈
        post_count = Post.objects.all().filter(posting_writer=user).count() # 글쓴이가 포스트 갯수

        # 유저가 쓴 포스트 출력
        post = Post.objects.all().filter(posting_writer=user)

        # 팔로워 버튼 위한 session 아이디
        session_id = request.session['username']
        session = MyUser.objects.get(username=session_id)
        session_id = session.id

        return render(request, 'people/profile.html', {'user':user, 'post':post ,'post_count':post_count, 'session_id':session_id})


# 프로필 수정
def profile_edit(request, id):
    user = MyUser.objects.get(pk=id) #user 객체 - instance 위해서 오픈

    if request.method == 'GET': #페이지 들어만 갔을 때
        form = ProfileEditForm(instance=user)
        return render(request, 'people/profile_edit.html', {'form':form})

    elif request.method == 'POST':
        if not request.FILES.get('user_photo'): # 사진 입력 안했으면
            user.user_nickname = request.POST['user_nickname']
            user.user_intro = request.POST['user_intro']
            user.save()
        else: # 사진 입력했으면
            user.user_photo = request.FILES.get('user_photo')
            user.user_nickname = request.POST['user_nickname']
            user.user_intro = request.POST['user_intro']
            user.save()
        return redirect('profile', id)


# 팔로우
def follow(request, follow_id):

    if request.method == 'GET':
        user = get_object_or_404(MyUser, pk=follow_id) # 내가 팔로우한 놈

        if user.follower.filter(pk=request.user.pk).exists(): # 내가 해당 유저를 팔로워 했으면
            user.follower.remove(request.user)
        else:
            user.follower.add(request.user)

        return redirect('profile', follow_id)

# 리스트에서 팔로우하는 기능
def list_follow(request, follow_id):

    if request.method == 'GET':
        user = get_object_or_404(MyUser, pk=follow_id) # 내가 팔로우한 놈

        if user.follower.filter(pk=request.user.pk).exists(): # 내가 해당 유저를 팔로워 했으면
            user.follower.remove(request.user)
        else:
            user.follower.add(request.user)

        return redirect('follow_list', follow_id)


# 팔로워 리스트 (나를 팔로우하는 사람들)
def follow_list(request, id):
    user = get_object_or_404(MyUser, pk=id)
    return render(request, 'people/follow_list.html', {'user':user})

# 팔로잉 리스트 (내가 팔로잉하는 사람들)
def following_list(request, id):
    user = get_object_or_404(MyUser, pk=id)
    return render(request, 'people/following_list.html', {'user':user})


# 저장한 게시글 보기
def saved_posting(request, id):
    if request.method == 'GET':
        user = MyUser.objects.get(pk=id) # user 객체 오픈
        post_count = Post.objects.all().filter(posting_writer=user).count() # 글쓴이가 포스트 갯수

        # 유저가 저장한 게시글
        bookmarks = user.bookmark.all()
        post = Post.objects.all().filter(pk__in=bookmarks).order_by('-posting_date')

        # 팔로워 버튼 위한 session 아이디
        session_id = request.session['username']
        session = MyUser.objects.get(username=session_id)
        session_id = session.id

        return render(request, 'people/profile.html', {'user':user, 'post':post ,'post_count':post_count, 'session_id':session_id})
