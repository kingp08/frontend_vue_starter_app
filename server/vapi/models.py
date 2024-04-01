from djongo import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, null=False)
    job_role = models.CharField(max_length=30, null=True)
    salary = models.FloatField(default=0)
    employee_registration = models.FloatField(default=0)