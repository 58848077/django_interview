from django.db import models

class Company(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    first_name =  models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
