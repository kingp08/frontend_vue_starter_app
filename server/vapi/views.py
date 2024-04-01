import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Employee

# Create your views here.

def getEmployees(request):
    employees = Employee.objects.values()
    data = json.dumps(list(employees))
    return HttpResponse(data, content_type='application/json')


def createEmployee(request):
    req_data = json.loads(request.body)
    print(req_data)
    employee = Employee.objects.create(name=req_data['name'], job_role=req_data['job_role'], salary=req_data['salary'], employee_registration=req_data['employee_registration'])
    employee.save()

    return HttpResponse(employee, content_type='application/json')

@csrf_exempt
def handleEmployees(request):
    if request.method == 'GET':
        return getEmployees(request)
    elif request.method == 'POST':
        return createEmployee(request)