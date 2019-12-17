from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord


# Create your views here.

def index(request):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpage_list}
    # my_dict={'inset_me':'Hello i am coming from first_app/views.py!'}
    return render(request,'first_app/index.html',context=date_dict)
