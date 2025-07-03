from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from bcuser.models import Bcuser
from django.http import Http404
from django.core.paginator import Paginator

# 게시글 목록
def board_list(request):
    all_boards=Board.objects.all().order_by('-id')
    page=int(request.GET.get('p', 1))
    paginator=Paginator(all_boards, 3)
    boards=paginator.get_page(page)
    return render(request, 'board_list.html', {'boards':boards})

# 게시글 작성
def board_write(request):
    if request.method == 'POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('user')
            bcuser=Bcuser.objects.get(pk=user_id)
            board=Board()
            board.title=form.cleaned_data['title']
            board.contents=form.cleaned_data['contents']
            board.writer=bcuser
            board.save()
            return redirect('/board/list/')
    else:
        form=BoardForm()

    # 로그인한 사용자만 게시글 작성 가능하도록 조건 추가
    if not request.session.get('user'):
        return redirect('/bcuser/login/')
    
    return render(request, 'board_write.html', {'form':form})

# 게시글 상세보기
def board_detail(request, pk): # pk(primary key): 게시물의 id
    # board=Board.objects.get(pk=pk)

    # 예외 처리
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist: # DoesNotExist: 요청한 객체가 존재하지 않는 경우
        raise Http404('※ 게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board':board})

# 게시글 수정
def board_update(request, pk):
    # 로그인 정보
    user_id=request.session.get('user')

    if not request.session.get("user"):
        return redirect("/bcuser/login/")

    try:
        # 게시글 정보
        board = Board.objects.get(pk=pk) 
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을수 없습니다.")
    
    # models의 참조조건이 설정되어 있으므로 값이 일치해야함
    if Bcuser.objects.get(pk=user_id) == board.writer:

        if request.method == "POST":
            form=BoardForm(request.POST)
            if form.is_valid():  # 폼의 데이터가 유효한 정보인지 여부
                user_id=request.session.get("user")  # 세션에서 로그인한 아이디 확보
                bcuser=Bcuser.objects.get(pk=user_id)  # 실제 데이터 베이스에서 로그인한 id 가져오기

                board.title=form.cleaned_data["title"]
                board.contents=form.cleaned_data["contents"]
                board.write=bcuser  # 글의 작성자
                board.save()
                return redirect("/board/list/")
        else:
            form=BoardForm(initial={"title": board.title, "contents": board.contents})   
    else:
        raise Http404("권한이 없습니다.")
    
    return render(request, "board_update.html", {"form": form})

# 게시글 삭제
def board_delete(request, pk):
    # 로그인한 계정(bcuser의 models에 write의 정보)
    user_id=request.session.get('user')

    # 예외처리
    if not request.session.get('user'):
        return redirect('/bcuser/login/')
    
    # 게시글 번호 가져오기
    board=Board.objects.get(pk=pk)

    if Bcuser.objects.get(pk=user_id) == board.writer:
        board.delete()
    else:
        raise Http404("권한이 없습니다. ")
    
    return redirect('/board/list')