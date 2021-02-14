# this file contain the all instruction which i used make this projct step by step
# in complete detail

1.  startproject CRUDfbvproject

2.startapp
3.templates folder
4. settings.py add path of templates and application

5.        models.py

from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=44)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)


6.  python manage.py makemigrations

7. register your model in database
           admin.py

           from django.contrib import admin
           from testapp.models import Employee
           # Register your models here.

           class EmployeeAdmin(admin.ModelAdmin):
               list_display=['eno','ename','esal','eaddr']

           admin.site.register(Employee,EmployeeAdmin)


8. python manage.py migrate

9. populate.py(create project based file)
-----create  fake data to use  this program----
=======>python pupulate.py(command prompt)


10.
==================views.py==============

from testapp.models import Employee
# Create your views here.

def retrieve_view(request):
    employee=Employee.objects.all()


11.
=================base.html==============

12.
================inddex.html============

13.
===========views.py============

from django.shortcuts import render
from testapp.models import Employee
# Create your views here.

def retrieve_view(request):
    employees=Employee.objects.all()
    return render (request,'testapp/index.html',{'employees':employees})


14.
============index.html============(update)

15.
===========urls.py===========
register your function views

16.Update ,insert and Delete Operation
========index.html==========(update)


17..
create file  Model based
=============forms.py============

from django import forms

from testapp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'


18.
create a html file for insert database
============create.html==============


19.
define view Function
============views.py=======

def create_view(request):
    form=EmployeeForm()
    return render(request,'testapp/create.html',{'form':form})

20.
define urls
========urls.py=============

21.
give that urls in index.html
  <a href="/create" class="btn btn-success btn-lg">Insert New Employees</a>

22.
update views.py=======


def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            #this will get the data from the form save into databases
    return render(request,'testapp/create.html',{'form':form})

this will form.save()
save your data in database

23.......
define views.py

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()

24.......
now define urls.py bit carefully and

url(r'^delete/(?P<id>\d+)/retrieve',views.delete_view),
.
.P should be capital
#\d  any digit  from 0 to 9
# \d+  atlest one digit
  127.0.0.1:8000/delete/1/retrieve

25.....
now define urls in html file which you created
======index.html===

<a href="/delete/{{emp.id}}/retrieve">Delete</a>

26......
views.py for update data from table

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee) <-----
        if form.is_valid():
            form.save()
            return redirect('/retrieve')

    return render (request,'testapp/update.html',{'employee':employee})

27.....
update.html make a file


28.......

now define urls.py bit carefully and

url(r'^update/(?P<id>\d+)/retrieve',views.update_view),
.
.P should be capital
#\d  any digit  from 0 to 9
# \d+  atlest one digit
  127.0.0.1:8000/delete/1/retrieve

  29.......

  now define urls in html file which you created
  for update urls
  ======index.html===

  <a href="/update/{{emp.id}}/retrieve">Update</a>
