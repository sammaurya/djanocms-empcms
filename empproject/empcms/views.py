from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class EmpUpdateView(UpdateView):
    model = Employee
    template_name = 'emp_update.html'
    fields = ['first_name', 'last_name', 'salary', 'date_of_join', 'phone']
    success_url = reverse_lazy('datatable')

class EmpDeleteView(DeleteView):
    model = Employee
    template_name = 'emp_delete.html'
    success_url = reverse_lazy('datatable')