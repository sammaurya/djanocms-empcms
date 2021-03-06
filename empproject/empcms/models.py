from django.db import models
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, default='', blank=True)
    # email = models.EmailField(null=False, blank=False)
    salary = models.IntegerField(null=False, blank=False)
    date_of_join = models.DateField()
    phone = models.IntegerField()
    entries = models.Count(emp_id)

    def __str__(self):
        return self.emp_id

    def get_absolute_url(self):
        return reverse('datatable')