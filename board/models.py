from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='제목'
    )
    contents = models.TextField(verbose_name='내용')
    
    # 사용자가 탈퇴시 그 사용자가 작성한 게시글 모두 삭제
    writer = models.ForeignKey(
        'bcuser.Bcuser', 
        on_delete=models.CASCADE, 
        verbose_name='작성자'
    )
    registered_dttm = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='등록시간'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'bootcampus_board'
        verbose_name = '솔데스크캠퍼스 게시글'
        verbose_name_plural = '솔데스크캠퍼스 게시글'