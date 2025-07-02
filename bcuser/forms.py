from django import forms
from django.contrib.auth.hashers import check_password
from .models import Bcuser

# forms.Form: 유효성 검사를 진행하는 클래스로 상속받아서 사용함
class LoginForm(forms.Form):
    username=forms.CharField(
        error_messages={
            'required':'사용자 이름을 입력해주세요'
        },
        max_length=32, label="사용자 이름")
    
    password=forms.CharField(
        error_messages={
        'required':'비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호")
    
    
    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')

        if username and password:
            try:
                bcuser=Bcuser.objects.get(username=username)
            except Bcuser.DoesNotExist:
                self.add_error('username', '존재하지 않는 아이디 입니다')
                return
            
            if not check_password(password, bcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.') 
            else:
                self.user_id=bcuser.id 