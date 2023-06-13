# url path mapping하는 곳 
from django.urls import path
from . import views_test

urlpatterns = [  
    path('',views_test.test_html_multi_data),     
    path('test_json',views_test.test_Json_data),   
    path('parameter_data',views_test.test_html_parameter_data),  
    path('parameter_data2/<int:my_id>',views_test.test_html_parameter_data2),  
    path('test_post',views_test.test_post_form), 
    path('test_post_handle',views_test.test_post_handle), 
    
]
# /test_json 으로 가게 된다. 
# path('주소',파일주소.함수명)
