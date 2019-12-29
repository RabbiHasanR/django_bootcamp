from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='Basic Injection!'
        return context

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School


class SchoolDetailview(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='basic_app/school_details.html'

class SchoolCreateView(CreateView):
    fields=('name','principle','location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principle')
    model=models.School


class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('basic_app:list')
