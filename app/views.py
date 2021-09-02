from django.shortcuts import render
import openpyxl
from .models import Employees
import re
from datetime import datetime

# Create your views here.
def Index(request):
    return render(request, 'pages/dashboard.html', {"title" : "Dashboard"})

def add_new(request):
    if request.method == 'GET':
        return render(request, 'pages/add_new.html', {"title": "Add New", "count":"", "total": ""})
    else:
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        excel_data = list()
        total = 0
        count = 0
        for row in worksheet.iter_rows():
            if total != 0:
                if is_valid_email(str(row[1].value)) and is_valid_phone(str(row[2].value)):
                    data = Employees(name=row[0].value, email=row[1].value, phone=str(row[2].value), dob=str(row[3].value), status="active")
                else:
                    data = Employees(name=row[0].value, email=row[1].value, phone=str(row[2].value), dob=str(row[3].value), status="inactive")
                    count += 1
                data.save()
            total += 1
        return render(request, 'pages/add_new.html', {"title": "Add New", "count":count, "total": total})

def valid_data(request):
    datas = Employees.objects.filter(status="active").values('name', 'email', 'phone', 'dob')
    data_list = []
    if datas:
        for data in datas:
            data_list.append(data)

    return render(request, 'pages/valid_data.html', {"title" : "Valid Data", "data_list": data_list})

def invalid_data(request):
    datas = Employees.objects.filter(status="inactive").values('name', 'email', 'phone', 'dob')
    data_list = []
    if datas:
        for data in datas:
            data_list.append(data)

    return render(request, 'pages/invalid_data.html', {"title" : "Invalid Data", "data_list": data_list})


def is_valid_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):
        return True
    else:
        return False

def is_valid_phone(phone):
    regex = re.compile("(0/91)?[6-9][0-9]{9}")
    return regex.match(phone)