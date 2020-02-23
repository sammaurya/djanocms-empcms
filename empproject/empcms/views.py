from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Employee
# Create your views here.

class EmpListView(ListView):
    model = Employee
    template_name = 'display_employee.html'

class EmpDetailView(DetailView):
    model = Employee
    template_name = 'emp_details.html'

class EmpCreateView(CreateView):
    model = Employee
    template_name = 'emp_add.html'
    fields = '__all__'