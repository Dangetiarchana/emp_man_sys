from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee

 

# Create your views here.
def index(request):
    return render(request, "index.html")
    


def view_emp(request):
    emps=Employee.objects.all()
    return render(request, "view_emp.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        add=request.POST['add']
        sal=request.POST['sal']
        new_emp=Employee(name=name,age=age,add=add,sal=sal)
        new_emp.save()
        return HttpResponse("new employee added succesfully <a href='view_emp'>go back</a>") 
    else:
        print("get method")
        return render(request,"add_emp.html")



def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)#return render(request, 'remove_emp.html', {'emps'=emps})
            emp_to_be_removed.delete()
            return HttpResponse("employee remove successfully")
        except:
            return HttpResponse("please enter a valid emp id")
    emps=Employee.objects.all()
    return render(request,'remove_emp.html',{'emps':emps})



def filter_emp(request):
    if request.method=="POST":
        name = request.POST["name"]
        
        
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(name__icontains=name)
        
        return render(request, "view_emp.html",{'emps':emps})
    return render(request,"filter_emp.html")

