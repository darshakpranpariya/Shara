from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shara/index.html')
    
def main(request):
    return render(request,'shara/main.html')

