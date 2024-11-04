from django.shortcuts import render, HttpResponse
from .models import demoDB
# Create your views here.
def home(request):
    return HttpResponse("what is a response")

def todos(request):
    items=demoDB.objects.all()
    return render(request, "db.html",{"todos": items})