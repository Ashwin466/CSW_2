from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# def home (request):
    # return HttpResponse("""
#                         <br><br><br><br><br>
# <center>


# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

# <table  border="1">

# 	<tr>
# 		<th>  Image  </th>
# 		<th>  Text  </th>
# 	</tr>
# 	<tr>
# 		<td>  <img src ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCZHeOeTJ3UVPCVUlgN1BmTn0KUNcCRvDsYQ&s"  width ="10%">    </td>

# 		<td> <h1> Ashwin </h1> </td>

# 	</tr>
#  </table>
#  </center>
#  </b>""")
# students=[
#     {'name':'Ashwin','regd':'24E110A33','sem':4},
#     {'name':'Ajit','regd':'24E125A04','sem':3},
#     {'name':'abc','regd':'24E113843','sem':2}
# ]
# users=[
#     {'uname':'Ashwin','mail':'ashwin@gmail.com','mobile':7978117254,'age':19,'pass':'Ashwin@hello'},
#     {'uname':'Ajit','mail':'ajitn@gmail.com','mobile':4825838264,'age':12,'pass':'ajit@hello'},
#     {'uname':'roshan','mail':'roshan@gmail.com','mobile':7854125963,'age':13,'pass':'roshan@hello'},
#     {'uname':'ritik','mail':'ritik@gmail.com','mobile':7458963254,'age':21,'pass':'ritik@hello'},
#     {'uname':'rishab','mail':'rishab@gmail.com','mobile':7856324189,'age':18,'pass':'rishab@hello'}

# ]
    # return render(request, "index.html", context={'students': students,'users': users})
def home(request):
    if request.method == "POST":
        data = request.POST
        emp_name = data.get("Emp_name")
        emp_email = data.get("Emp_Email")
        emp_mobile = data.get("Emp_Mobile")

       
        if Employee.objects.filter(Emp_Email=emp_email).exists():
            messages.error(request, "Email already exists")
            return redirect('/')

        Employee.objects.create(
            Emp_name=emp_name,
            Emp_Email=emp_email,
            Emp_Mobile=emp_mobile
        )
        return redirect('/')

    query = Employee.objects.all()
    context = {'employee': query}
    return render(request, "index.html", context)

def delete(request, id):
    query_1 = Employee.objects.get(id=id)
    query_1.delete()
    return redirect('http://127.0.0.1:8000/')

def update(request, id):
    if request.method=="POST":
        data = request.POST
        emp_id = data.get("Emp_id")
        emp_name = data.get("Emp_name")
        emp_email = data.get("Emp_Email")
        emp_mobile = data.get("Emp_Mobile")
        q1 = Employee.objects.filter(id=emp_id).update(
            Emp_name = emp_name,
            Emp_Email = emp_email,
            Emp_Mobile = emp_mobile
        )
        return redirect('http://127.0.0.1:8000/')
    query1 = Employee.objects.get(id=id)
    context = {'emp_update' : query1}
    return render(request,"update.html",context)

    
def success (request):
    return HttpResponse("<h1> Success Page </h1>")
def success1 (request):
    return render (request , "success.html")