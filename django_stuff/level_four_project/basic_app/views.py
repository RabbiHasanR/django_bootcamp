from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    my_dir={'text':'Hi I Am Rabbi.','number':100}
    return render(request,'basic_app/index.html',my_dir)
@login_required
def special(request):
    return HttpResponse('You are logged in,Nice!')    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.picture=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            print(user.errors,profile.errors)
    else:
        user=UserForm()
        profile=UserProfileInfoForm()
    return render(request,'basic_app/registration.html',{'user_form':user,'profile_form':profile,'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Acount Not active')
        else:
            print('Some one tried to login and ailed')
            print('username:{} and password:{}'.format(username,password))
            return HttpResponse('Invalid login details suplied!')
    else:
        return render(request,'basic_app/login.html',{})
