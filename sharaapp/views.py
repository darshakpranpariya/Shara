from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate

def index(request):
    return render(request,'shara/index.html')
    
def main(request):
    print("hello")
    if request.method == 'POST':
        print("hellooooooo")
        signup_data = request.POST.dict()
        username = signup_data.get("uname")
        email = signup_data.get("email")
        password = signup_data.get("psw")
        dic = {'name':username}
        if(username is not None and email is not None and password is not None):
            if(User.objects.filter(username=username).exists()):
                messages.error(request, "Username is already exists.")
            elif(User.objects.filter(email=email).exists()):
                messages.error(request, "Email is already exists.")
            else:
                ob1 = User.objects.create_user(username=username,email=email,password=password)
                ob1.save()
                messages.success(request, "you are successfully registered.")
                messages.info(request, "please, do login.")
                return render(request,'shara/main.html')
        else:
            if(username is not None):
                user = authenticate(username=username, password=password)
                if(user is not None):
                    messages.success(request, "LogIn Successful")
                    print(dic['name'])
                    return render(request,'shara/main.html',dic)
                else:
                    messages.error(request, "Username/Password is wrong.")
                    return render(request,'shara/main.html')
            else:
                user = authenticate(email=email, password=password)
                if(user is not None):
                    messages.success(request, "LogIn Successful")
                    return render(request,'shara/main.html')
                else:
                    messages.error(request, "Email/Password is wrong.")
                    return render(request,'shara/main.html')
    return render(request,'shara/main.html')

# def signup(request):
#     if request.method == 'POST':
#         print("hello")
#         signup_data = request.POST.dict()
#         username = signup_data.get("uname")
#         email = signup_data.get("email")
#         password = signup_data.get("psw")
#         ob1 = User.objects.create_user(username=username,email=email,password=password)
#         ob1.save()
#         return render(request,'shara/index.html')
#     return render(request,'shara/index.html')