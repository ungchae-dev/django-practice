from django.db import models

# Create your models here.

class Bcuser(models.Model):
    # verbose_name : 한글 이름
    username=models.CharField(max_length=32, verbose_name='사용자명')
    useremail=models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password=models.CharField(max_length=64, verbose_name='비밀번호')
    # auto_now_add : 현재시간 적용
    registered_dttm=models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    # username 생성 시 문자열 함수를 이용해 객체 username으로 반환
    def __str__(self) :
        return self.username
    
    #  Table Name
    class Meta:
        db_table='soldesk_bcuser'
        verbose_name='솔데스크 사용자'
        verbose_name_plural='솔데스크 사용자'