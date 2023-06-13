from django.db import models

# Create your models here.
# models.py의 클래스와 DB의 table과 sync를 맞춰 테이블 컬럼정보 자동생성

# class name = table name ,  변수 = column name
class Test(models.Model):
   name = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 
   password = models.CharField(max_length=20)