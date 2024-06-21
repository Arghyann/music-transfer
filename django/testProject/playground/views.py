from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_something(request):
    x=1
    y=2
    return render(request,"hello.html",{"name":"Aryan"})

def room(request):
    return render(request,"room.html")