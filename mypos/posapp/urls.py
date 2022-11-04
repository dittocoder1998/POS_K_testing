from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name = 'sign_up'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('add_cust', views.add_customer, name = 'add_cust'),
    # path('custLand', views.custLand, name = "custLand"),
    # path('adminEmp', views.adminEmp, name = "adminEmp"),
    path('adminVend', views.adminVend, name = "adminVend"),
    path('empTrans', views.empTrans, name = "empTrans"),
    path('custRep', views.custRep, name = "custRep"),
    path('EmpHome', views.EmpHome, name='EmpHome'),
    path('shop', views.shop, name='shop'),
    path('custTrans', views.custTrans, name='custTrans'),
    path('empTable',views.empTable, name="empTable"),
    path('custTable',views.custTable, name="custTable"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('deleteEmp/<int:id>', views.deleteEmp, name='deleteEmp'),
    # path('CustomerLanding', views.cust_landing, name = "CustomerLanding")
]
