from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import Bcuser

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # requset로 받을때 넘어오는 값이 없으면 nullpoint error가 발생되므로 None처리
        username=request.POST.get('username', None)
        useremail=request.POST.get('useremail', None)
        password=request.POST.get('password', None)
        re_password=request.POST.get('re-password', None) 

        res_data={}

        if not(username and useremail and password and re_password):
            res_data['error']="모든 값을 입력해야합니다."
        elif password != re_password:
            res_data['error']="비밀번호가 일치하지 않습니다."
        else:
        # 입력받은 값을 변수방에 저장하여(username, password) 데이터베이스에(models) 전달
            bcuser=Bcuser(
                username=username, 
                useremail=useremail, 
                password=make_password(password) # make_password: 비밀번호 암호화 처리
                )
            bcuser.save() # 저장

        return render(request, 'register.html', res_data)