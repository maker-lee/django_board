from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test


# Create your views here.

# get 요청 시 html 파일 그대로 return한다
def test_html(request) :
    return render(request, 'test/test.html')

# get 요청 시 html + data return
def test_html_data(request) :
    my_name = "Lee"
    return render(request, 'test/test.html',{'name':my_name})
# name:my_name을 딕셔너리 형태로 던져주게 된다. 


# get 요청 시 html + multi data return (json느낌의... 그러나 템플릿엔진인..)
def test_html_multi_data(request) :
    data = {
        'name' : "Lee",
        'age' : 20
    }   
    return render(request, 'test/test.html',{'data':data})
# 'data' = key data = values 


# get 요청 시 html + data return
def test_Json_data(request) :
    data = {
        'name' : "Lee",
        'age' : 20
    }    
    return JsonResponse(data)
# render는 웹개발에서 화면을 return해줄때 사용하는 용어다.
# 그냥 리턴하면 파이썬의 자료 형태이므로 변환을 해줘야한다. 파이썬에 dict와 유사한 json형태로 변환해서 return한다.

# 사용자가 get방식으로 쿼리파라미터 방식 데이터를 넣어놓을 때
# 1. 쿼리 파라미터 방식 : localhost:8000/author?id=10&name=lee
# 2. pathvariable 방식 (현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data(request) :
    id = request.GET.get('id')
    name = request.GET.get('name')
    print(id)
    print(name)
    return render(request, 'test/test.html',{})
# GET방식 > get 꺼내온다 정보 안에서 id 정보를  


# 사용자가 get방식으로 쿼리파라미터 방식 데이터를 넣어놓을 때
# 1. 쿼리 파라미터 방식 : localhost:8000/author?id=10&name=lee
def test_html_parameter_data(request) :
    myname = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    data = {
        'name': myname,
        'email' : email,
        'password' : password
    }
    return render(request, 'test/test.html',{'data':data})
# 그냥 리턴하면 파이썬의 자료 형태이므로 변환을 해줘야한다. 파이썬에 dict와 유사한 json형태로 변환해서 return한다.

# http://도메인/파일의 지정?이름1=값1&이름2=값2& ...

# urls 수정
#    path('parameter_data2/<int:>my_id',views_test.test_html_parameter_data2), 


# 사용자가 get방식으로 쿼리파라미터 방식 데이터를 넣어놓을 때
# 2. pathvariable 방식 (현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data2(request, my_id) :
    print(my_id)
    return render(request, 'test/test.html',{})


# form 태그를 활용한 post 방식

# def test_post_form(request): 아래와 합침
#     return render(request, 'test/test_post_form.html')

# POST방식
def test_post_handle(request):
    if request.method == 'POST' :
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        
        # DB에 insert -> save 함수를 사용함 .
        # DB에 테이블과 sync가 맞는 Test클래스에서 객체를 만들어서 save
        t1 = Test() # class를 깡통으로 만들고
        t1.name = user_name # 이렇게 집어넣는 스타일로 함 
        t1.email = user_email
        t1.password = user_password
        t1.save()

        return redirect('/') # http://localhost:8000/ 으로 이동해라 
        #post 요청은 요청 후 적절한 상태코드를 줘야 한다.get처럼 html 화면 응답을 줄게 없으니 200 이런거. 
        # return HttpResponse('가입을 축하드립니다') 을 redirect로 변경함
    else : # GET방식
       return render(request, 'test/test_post_form.html')# 화면을 rendering(화면 리턴) 해주는 method 필요
 

# DB에서 조회하기 
def test_select_one(request,my_id) : # 하나만 조회하기, 단 건 조회는 get()함수
    t1 = Test.objects.get(id=my_id)  
    return render(request, 'test/test_select_one.html',{'data':t1})

def test_select_all(request) : # 전체 조회하기, 모든 data조회는 post, select * from ..; all()함수를 사용한다. 파라미터 받을 필요 없음
    tests = Test.objects.all() 
    return render(request, 'test/test_select_all.html',{'datas':tests})

# WHERE 조건으로 조회할 때는 filter() 함수를 사용한다. 
def test_select_filter(request) :
    my_name = request.GET.get('name')
    tests = Test.objects.filter(name=my_name)
    return render(request, 'test/test_select_filter.html',{'datas':tests})

# UDATE 하기 
def test_update(request):
    if request.method == 'POST' : 
        my_id = request.POST['my_id'] # my_id로 id가 작성한 '기존 객체' 조회
        t1 = Test.objects.get(id=my_id) # db에서 객체를 조회해서 가져오기         
        user_name = request.POST['user_name'] # 사용자가 입력한 값으로 업데이트
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']

        t1.name = user_name 
        t1.email = user_email
        t1.password = user_password
        t1.save() # 기존 건이 있으면 update가 되고 없으면 insert가 된다. 
        return redirect('/') 
    else : 
       return render(request, 'test/test_update.html')
    
