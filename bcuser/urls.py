from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register), # views.py의 register 함수 호출
]