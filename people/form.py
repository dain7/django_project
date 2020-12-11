from django import forms
from member.models import MyUser


# 프로필 수정 폼
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['user_photo', 'user_nickname', 'user_intro']
