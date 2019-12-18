from django.shortcuts import render

# Create your views here.

def index(request):
    my_dir={'text':'Hi I Am Rabbi.','number':100}
    return render(request,'basic_app/index.html',my_dir)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')
