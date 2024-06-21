from django.urls import path

from . import views 
urlpatterns=[
    path('hello/',views.say_something),
    path("room",views.room)
]