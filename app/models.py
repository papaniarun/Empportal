from django.db import models
from django.utils.timezone import now

class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    dob = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(default=now, editable=False)