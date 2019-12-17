from django.shortcuts import render
from user_profile.models import User
from user_profile.forms import FormName

# Create your views here.
def welcome(request):
    return render(request,'user_profile/welcome.html',context=None)

def users(request):
    user_list=User.objects.all()
    user_dic={'users':user_list}
    return render(request,'user_profile/user.html',context=user_dic)

def form_name_view(request):
    form=FormName()

    if request.method=='POST':
        form=FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('Error form invalid')

    return render(request,'user_profile/forms_page.html',{'form':form})
