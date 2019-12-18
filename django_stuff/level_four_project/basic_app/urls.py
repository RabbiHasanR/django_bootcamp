from django.urls import path
from basic_app.views import index,other,relative,register,user_login

#template tagging

app_name='basic_app'
urlpatterns = [
    path('other/', other,name='other'),
    path('relative/', relative,name='relative'),
    path('registration/', register,name='registration'),
    path('login/', user_login,name='user_login'),
]
