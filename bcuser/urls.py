from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register), # views.py의 register 함수 호출
    path('login/', views.login),  # login, 로그인
    path('logout/', views.logout) # logout, 로그아웃
]