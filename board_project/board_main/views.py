from django.shortcuts import render , redirect 
from .models import Author, Post

# Create your views here.

def home(request) : #home.html로 이동한다. 
    return render(request,'home.html')

def author_list(request) : # 회원 가입한 사람들 전체 조회 
    authors = Author.objects.all() 
    return render(request,'author/author_list.html',{'authors':authors})

def author_detail(request,my_id) : # 상세조회 페이지로 이동한다. 
    author = Author.objects.get(id=my_id) 
    return render(request,'author/author_detail.html',{'author':author})

def post_list(request) : # 회원 목록으로 이동한다. 
    return render(request,'post/post_list.html')

def author_update(request,my_id) : #회원정보수정 페이지에서 동작 
    author = Author.objects.get(id=my_id) # 웹을 뿌려주기 전에 조회
    if request.method == 'POST' :        
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']        
        author.name = user_name 
        author.email = user_email
        author.password = user_password
        author.save()
        return redirect('/') 
    else : 
        return render(request, 'author/author_update.html',{'author':author})#


def author_new(request) : # 회원 가입 페이지에서 동작
    if request.method == 'POST' :
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']        
        a1 = Author() 
        a1.name = user_name 
        a1.email = user_email
        a1.password = user_password
        a1.save()
        return redirect('/') 
    else : 
       return render(request,'author/author_new.html')
    





