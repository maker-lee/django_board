from django.shortcuts import render , redirect 
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def home(request) : #home.html로 이동한다. 
    return render(request,'home.html')

def author_list(request) : # 회원 가입한 사람들 전체 조회 
    authors = Author.objects.all() 
    return render(request,'author/author_list.html',{'authors':authors})


def author_detail(request,my_id) : # 상세조회 페이지로 이동한다. 
    author = Author.objects.get(id=my_id) 
    #print(author.posts.count()) # 몇개의 글을 썼는지 카운트 
    return render(request,'author/author_detail.html',{'author':author})


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
    


def post_list(request) : # 게시글 전체 조회 -> 게시물 목록으로 이동한다. 
    posts = Post.objects.filter().order_by('-created_at') # 게시물 작성 시간 역순 정렬
    #author = Author.objects.get(email=user_email) 
    return render(request,'post/post_list.html',{'posts':posts})


def post_new(request) : # 게시물 입력 페이지에서 동작
    if request.method == 'POST' :
        user_title = request.POST['user_title']
        user_contents = request.POST['user_contents']  
        user_email = request.POST['user_email']  
        p1 = Post() 
        #try:
        if user_email :
            try:
                a1 = Author.objects.get(email=user_email) #DB에서 Author를 조회해서 email을 불러옴
                p1.author = a1 # 이 안에는 {id:1,name:'kim'..} 객체가 들어가있음 
                # 장고에서 a1객체에서 id값만 빼고 db에 저장할 때는 author_id에 id값을 저장함. 조회와 insert sync를 맞추기 위해서 models.py author처럼 author 객체로 입력 
            except Author.DoesNotExist :
                # HttpResponse 200ok 로 반환된다. 에러인데.. ㅜ
                return HttpResponseNotFound('존재하지 않는 이메일입니다.')
            
        p1.title = user_title 
        p1.contents = user_contents
        p1.save()
        return redirect('/') 
    else : 
       return render(request,'post/post_new.html')
    

def post_detail(request,my_id) : # 게시판 상세조회 페이지로 이동한다. 
    post = Post.objects.get(id=my_id) 
    return render(request,'post/post_detail.html',{'post':post})


def post_update(request,my_id) : # 게시판 상세조회 페이지에서 수정 후 동작 
    post = Post.objects.get(id=my_id) # 웹을 뿌려주기 전에 조회
    if request.method == 'POST' :        
        user_title = request.POST['user_title']
        user_contents = request.POST['user_contents']  
        post.title = user_title 
        post.contents = user_contents
        post.save()
        return redirect('/') 
    else : 
        return render(request, 'post/post_update.html',{'post':post})#

