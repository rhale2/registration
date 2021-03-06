from django.shortcuts import render
from django.http import HttpResponse
from .serilaizers import *
from rest_framework import generics 
from django.views.generic import ListView
from django.views.generic import CreateView

def index(request):
    return HttpResponse("Hello world from django backend");

class StudentListView(generics.ListCreativeAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentListForm (ListView):
    model = Student
    
class StudentCreateForm (CreateView, ListView):
    model = Student
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']
