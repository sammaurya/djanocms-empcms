
from django.conf.urls import url, include
from .views import EmpListView, EmpCreateView
urlpatterns = [
    url(r'^emp_add', EmpCreateView.as_view(), name='emp_add'),
    url(r'^', EmpListView.as_view(), name='datatable'),

]