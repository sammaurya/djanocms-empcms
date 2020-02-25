from django.urls import path
from django.conf.urls import url, include, re_path
from .views import EmpListView, EmpCreateView, EmpUpdateView, EmpDeleteView
urlpatterns = [
    url(r'^emp_add', EmpCreateView.as_view(), name='emp_add'),
    path('emp_update/<slug:pk>/', EmpUpdateView.as_view(), name='emp_update'),
    path('emp_delete/<slug:pk>/', EmpDeleteView.as_view(), name='emp_delete'),
    url(r'^', EmpListView.as_view(), name='datatable'),

]