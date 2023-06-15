# url path mapping하는 곳 
from django.urls import path
from . import views_test, views

urlpatterns = [  
    # path('',views_test.test_html_multi_data),     
    # path('test_json',views_test.test_Json_data),   
    # path('parameter_data',views_test.test_html_parameter_data),  
    # path('parameter_data2/<int:my_id>',views_test.test_html_parameter_data2),  
    # path('test_post_handle',views_test.test_post_handle), 
    # path('test_select_one/<int:my_id>',views_test.test_select_one),
    # path('test_select_all',views_test.test_select_all),
    # path('test_select_filter',views_test.test_select_filter),
    # path('test_update',views_test.test_update), 

    path('',views.home),
    path('authors/',views.author_list),
    path('author/new',views.author_new),
    path('author/<int:my_id>',views.author_detail),
    path('author/<int:my_id>/update',views.author_update), 
    
    path('posts/',views.post_list),
    path('post/new',views.post_new),
    path('post/<int:my_id>',views.post_detail),
    path('post/<int:my_id>/update',views.post_update),
    
    ]

 
# path('주소',파일주소.함수명)
# http://localhost:8000/주소 

'''
Method: POST/GET 
Code : http 상태 코드 200 번대는 정상 / 300번대는 redirect코드 / 400번대 사용자 문제 / 500번대 서버 문제 , post는 대부분 300번대를 사용함. ex) 회원가입 후 summit을 하고 다른 곳으로 보내주지 않으면 성격급한 사용자가 계속 summit 시도함.

프론트엔드와 서버가 나누어져 있는 경우 상태 코드가 중요하다. 왜?
프론트엔드는 3000번 포트고 백엔드가 8000번 포트로 떠있는 경우, 지금 연습 하고 있는건 다 8000번대임

사용자와 서버 간에는 request와 response를 주고 받는다. 요청-응답
요청과 응답은 정해진 프로토콜(약속)에 의해 통신이 이루어져야 하고 이 프로토콜을 http 프로토콜이라고 한다.
header와 body로 이루어져있다.
hedaer에는 url, port 등 주요 요약정보가 담겨 있고
body에는 본문 내용이 담겨있다. get은 header에 요청하는 정보를 담고, post는 요청하는 정보를 body에 담는다. requset body는 내용 공개가 되지 않는다. header는 확인이 가능하다.
'''