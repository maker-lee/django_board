from django.db import models
from django.utils import timezone

# views_test.py 에서 import하여 사용했다. 
# Create your models here.
# models.py의 클래스와 DB의 table과 sync를 맞춰 테이블 컬럼정보 자동생성

# class name = table name ,  변수 = column name
class Test(models.Model):
   name = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 
   password = models.CharField(max_length=20)


class Author(models.Model) :
   name = models.CharField(max_length=20) 
   email = models.CharField(max_length=50) 
   password = models.CharField(max_length=30)
   # DB설정에 default timestamp가 걸리는게 아니라,장고가 현재 시간을 db에 insert 
   created_at = models.DateTimeField(auto_now_add=True) # default : current_timestamp
   updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model) :
   title = models.CharField(max_length=100) 
   contents = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True) # default : current_timestamp, default=timezone.now()
   updated_at = models.DateTimeField(auto_now=True)
   # DB에는 fk를 설정한 변수명에 _id가 붙게 된다
   author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL) # author 객체가 들어옴 
   # null=True 이면, Empty 값을 DB에 NULL로 저장한다. DB에서 Null이 허용된다. set_null 설정해준다
   # view_count = models.IntegerField(default=0) # 카운트 