from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"), #return the home function from views when you call nothing 
    path("todo/" , views.todos, name="todos")
]
