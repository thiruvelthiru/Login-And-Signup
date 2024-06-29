from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Datas


# Create your views here.

def home(request):
    return render(request,"index.html")

def login (request):
    return render(request,"login.html")

def register(request):
    if request. method == "POST" :
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password==confirm_password:
            user=objects.create_user(username=name,email=email,password=password)
            user.save()
            messages.success(request,'Your account has been crated successfully..!')
            return redirect('login')
        else:
            messages.warning(request,'password mismatching..!!!!')
            return redirect('register')
        
        obj=Datas()
        obj.username = username
        obj.email = email
        obj.password = password
        obj.password = confirm_password
        obj.save()  
        mydata= Datas.objects.all()
        return redirect('')
    else:
        return render(request,"register.html")