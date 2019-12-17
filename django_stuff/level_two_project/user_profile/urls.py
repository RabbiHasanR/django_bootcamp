from django.urls import path
from user_profile.views import welcome,users,form_name_view

urlpatterns=[
    path('',welcome,name='welcome'),
    path('users/',users,name='users'),
    path('signup/',form_name_view,name='form')
]
