from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list), # 게시글 목록: list로 요청이 오면 views.board_list 함수 호출
    path('write/', views.board_write), # 게시글 작성
    path('detail/<int:pk>/', views.board_detail), # 게시글 1개 상세보기
    path('update/<int:pk>/', views.board_update), # 게시글 수정
    path('delete/<int:pk>/', views.board_delete) # 게시글 삭제
]
