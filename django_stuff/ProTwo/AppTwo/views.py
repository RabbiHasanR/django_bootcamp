from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    my_dic={'help':'Please help me.I am coming from AppTwo/views.py!'}
    return render(request,'AppTwo/help.html',context=my_dic)
