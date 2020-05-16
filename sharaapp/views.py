from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import *
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth import authenticate
from  sharaapp.models import *
import datetime
from django.shortcuts import HttpResponseRedirect

def index(request):
    return render(request,'shara/index.html')
    
def main(request):
    alltips= Tips.objects.all()
    context= {'alltips': alltips}
    if request.method == 'POST':
        signup_data = request.POST.dict()
        username = signup_data.get("uname")
        email = signup_data.get("email")
        password = signup_data.get("psw")
        if(username is not None and email is not None and password is not None):
            if(User.objects.filter(username=username).exists()):
                messages.error(request, "Username is already exists.")
            elif(User.objects.filter(email=email).exists()):
                messages.error(request, "Email is already exists.")
            else:
                ob1 = User.objects.create_user(username=username,email=email,password=password)
                ob1.save()
                p = User.objects.get(username=username)
                ob2 = DeepUserDetails(userid_id=p.id,reputation=0,totalupvote=0,totaldownvote=0,totaltips=0)
                ob2.save()
                messages.success(request, "you are successfully registered.")
                messages.info(request, "please, do login.")
                return render(request,'shara/main.html')
        else:
            if(username is not None):
                user = authenticate(username=username, password=password)
                if(user is not None):
                    messages.success(request, "Login Successful")
                    login(request, user)
                    return render(request,'shara/main.html',context)
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
    return render(request,'shara/main.html',context)

def profile(request):
    if request.user.is_authenticated:
        return render(request,'shara/profile.html')
    else:
        messages.warning(request,"Please, consider to do login first")
        return HttpResponseRedirect('/main/')

def logout(request):
    django_logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect('/main/')

def addtips(request):
    if request.method == 'POST':
        tips_data = request.POST.dict()
        tag = tips_data.get("tag")
        comment = tips_data.get("comment")
        link = tips_data.get("link")
        file = request.FILES['file']
        userid = request.user;
        ob = Tips(userid_id=userid.id,tags=tag,comment=comment,links=link,file=file,date=datetime.datetime.now(),upvote=0,downvote=0,totalscore=0)
        ob.save()
        u = DeepUserDetails.objects.get(userid_id=userid.id)
        u.totaltips+=1
        u.save()
        messages.info(request,"Your tips uploaded successfully!")
        return HttpResponseRedirect('/profile/')
    return render(request,'shara/profile.html')
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