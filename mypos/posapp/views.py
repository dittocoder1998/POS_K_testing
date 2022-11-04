from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from .models import Employee
from .models import Customer
from django.template import loader
from django.urls import reverse
#from posapp.models import Employee

# from POS.models import Departments, Employees
# from POS.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

# Renders html code
# def index(request):
#     return render(request, 'base.html')

# Tylers part below

@login_required(login_url = '/login')

def home(request):
    return render(request, 'home.html')

def EmpHome(request):
    return render(request, 'EmpHome.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

def add_emp(request):
    form = EmployeeForm
    submitted = False

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_emp')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'employee.html', {'form': form, 'submitted': submitted})


def add_customer(request):
    form = CustomerForm
    submitted = False

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_cust')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'customer.html', {'form': form, 'submitted': submitted})

def custLand(request):
    return render(request, 'CustomerReport/CustomerLanding.html')

# def adminEmp(request):
#     return render(request, 'AdminReport/AdminEmployee.html')

def adminVend(request):
    return render(request, 'AdminReport/AdminVendor.html')

def empTrans(request):
    return render(request, 'EmployeeReport/EmployeeTransactions.html')

def custRep(request):
    return render(request, 'EmployeeReport/EmployeeTransactions.html')

def shop(request):
    return render(request, 'shop.html')

def custTrans(request):
    return render(request, 'CustomerReport/CustomerLanding.html')

def empTable(request):
    mydata = Employee.objects.all()
    template = loader.get_template('AdminReport/AdminEmployee.html')
    context = {
        'employees': mydata,
    }
    return HttpResponse(template.render(context, request))

def custTable(request):
    mydata = Customer.objects.all()
    template = loader.get_template('CustomerReport/CustomerLanding.html')
    context = {
        'customers': mydata,
    }
    return HttpResponse(template.render(context, request))

def delete(request, id):
  member = Customer.objects.get(cust_id=id)
  member.delete()
  return HttpResponseRedirect(reverse('custTable'))

def deleteEmp(request, id):
  member = Employee.objects.get(emp_id=id)
  member.delete()
  return HttpResponseRedirect(reverse('empTable'))