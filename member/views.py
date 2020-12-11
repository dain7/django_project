from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import MyUser
from django.contrib import auth
from django.db import IntegrityError


# Create your views here.

# 회원가입
def signup(request):
    res_data = {}
    try:
        if request.method == "GET":
            return render(request, 'member/signup.html')


        elif request.method == "POST":
            user_id = request.POST['username']
            user_password = request.POST['password1']
            user_nickname = request.POST['user_nickname']

            if not (user_id and user_password and user_nickname): # 모든 항목을 안적었을 경우
                res_data['error'] = "모두 안 채워넣으면 가입 안시켜줌"
                return render(request, 'member/signup.html', res_data)
            else: # 모든 항목을 적었는데
                if request.POST['password1'] != request.POST['password2']:
                    res_data['error'] = "비밀번호가 서로 다릅니다!!!"
                    return render(request, 'member/signup.html', res_data)
                else:
                    user = MyUser.objects.create_user(
                    username=user_id, password=user_password, user_nickname=user_nickname
                    )
                    return redirect('/')
        return redirect('/')
    except IntegrityError:
        res_data['error'] = "이미 존재하는 아이디입니다."
        return render(request, 'member/signup.html', res_data)

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['user_password']

        res_data = {}

        user = auth.authenticate(request, username=username, password=password)

        if user is not None: # 해당 유저 객체가 있다면
            request.session['username'] = username
            request.session['user_password'] = password
            auth.login(request, user)
            return redirect('/')
        else:
            res_data['error'] = "아이디 혹은 비밀번호가 다릅니다~!"
            return render(request, 'member/login.html', res_data)

    elif request.method == 'GET':
        user_id = request.session.get('username')
        if user_id: # 이미 로그인이 되어있을 경우
            return redirect('/')
        else: # 로그인이 안되어있을 경우
            return render(request, 'member/login.html')

# 로그아웃
def logout(request):
    if request.method == "GET":
        request.session.clear()
        auth.logout(request)
    return redirect('/accounts/login/')


# # def login(request):
# #     if request.method == "GET":
# #         user_id = request.session.get('user_id')
# #
# #         if user_id: # 이미 로그인이 되어있을 경우
# #             res_data = {}
# #             res_data['error'] = "이미 로그인 되어있습니다"
# #             return render(request, 'member/done.html', res_data)
# #         else: # 로그인이 안되어있을 경우
# #             return render(request, 'member/login.html')
# #
# #     elif request.method == "POST":
# #         user_id = request.POST.get('user_id')
# #         user_password = request.POST.get('user_password')
# #         res_data = {}
# #
# #         if not (user_id and user_password):
# #             res_data['error'] = "아이디 혹은 비밀번호를 입력하세요!!!"
# #             return render(request, 'member/login.html', res_data)
# #         else:
# #             myuser = User.objects.get(user_id = user_id)
# #
# #             if user_password == myuser.user_password:
# #                 # request.session['user_id'] = myuser.user_id
# #                 # request.session['user_nickname'] = myuser.user_nickname
# #                 user = auth.authenticate(request, username=user_id, password=user_password)
# #                 auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
# #                 return redirect('/')
# #             else:
# #                 res_data['error'] = "비밀번호 다른디유?"
# #                 return render(request, 'member/login.html', res_data)


# def login(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         user_password = request.POST['user_password']
#         res_data = {}
#
#         user = auth.authenticate(request, username = user_id, password = user_password)
#
#         if user is not None: # 해당 유저 객체가 있다면
#             auth.login(request, user)
#             return redirect('/')
#         else: # 해당 유저 객체가 없다면
#             res_data['error'] = "아이디 혹은 비밀번호가 틀렸습니다"
#             return render(request, 'member/login.html', res_data)



# def register(request):
#     if request.method == "GET":
#         return render(request, 'member/signup.html')
#
#     elif request.method == "POST":
#         user_id = request.POST.get('user_id')
#         user_password = request.POST.get('user_password')
#         # user_password = make_password(request.POST.get('user_password'))
#         user_nickname = request.POST.get('user_nickname')
#         res_data = {}
#
#         if not (user_id and user_password and user_nickname):
#             res_data['error'] = "모두 안 채워넣으면 가입 안시켜줌"
#             return render(request, 'member/signup.html', res_data)
#         else:
#             # user = User(user_id=user_id, user_password=make_password(user_password), user_nickname=user_nickname)
#             user = User.objects.create_user(
#             username=user_id, password=user_password, user_nickname=user_nickname
#             )
#             # user = User(user_id=user_id, user_password=user_password, user_nickname=user_nickname)
#             # user.save()
#         return redirect('/')
#
#

#
#     else:
#         user_id = request.session.get('user_id')
#
#         if user_id: # 이미 로그인이 되어있을 경우
#             res_data = {}
#             res_data['error'] = "이미 로그인 되어있습니다"
#             return render(request, 'member/done.html', res_data)
#         else: # 로그인이 안되어있을 경우
#             return render(request, 'member/login.html')
#
# # def login(request):
# #     if request.method == "GET":
# #         user_id = request.session.get('user_id')
# #
# #         if user_id: # 이미 로그인이 되어있을 경우
# #             res_data = {}
# #             res_data['error'] = "이미 로그인 되어있습니다"
# #             return render(request, 'member/done.html', res_data)
# #         else: # 로그인이 안되어있을 경우
# #             return render(request, 'member/login.html')
# #
# #     elif request.method == "POST":
# #         user_id = request.POST.get('user_id')
# #         user_password = request.POST.get('user_password')
# #         res_data = {}
# #
# #         if not (user_id and user_password):
# #             res_data['error'] = "아이디 혹은 비밀번호를 입력하세요!!!"
# #             return render(request, 'member/login.html', res_data)
# #         else:
# #             myuser = User.objects.get(user_id = user_id)
# #
# #             if user_password == myuser.user_password:
# #                 # request.session['user_id'] = myuser.user_id
# #                 # request.session['user_nickname'] = myuser.user_nickname
# #                 user = auth.authenticate(request, username=user_id, password=user_password)
# #                 auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
# #                 return redirect('/')
# #             else:
# #                 res_data['error'] = "비밀번호 다른디유?"
# #                 return render(request, 'member/login.html', res_data)
#
# def logout(request):
#     request.session.clear()
#     return redirect('/accounts/login/')
