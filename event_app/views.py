
from email import message
from tkinter import FLAT
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from event_app.forms import  UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from service_app.views import home
from.forms import EventListForm 
from service_app.models import EventList
from .models import BookedList

# Create your views here


def first(request):
    event=EventList.objects.all()
    return render(request, "home.html",{"event":event})


def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Taken")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is Already taken")
                return redirect("signup")
            else:
                new_user=form.save()
                new_user.save()
                messages.info(request,"New user Created")
                return redirect('signin')

    return render(request, "signup.html", {"form": form})


def signin(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            group=None
            if request.user.groups.exists():
                group=user.groups.all()[0].name
                print(group)
                if group=="customers":
                    request .session["username"]=username
                    request .session["password"]=password
                    login(request,user)
                    return redirect("first")
                
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("signin")

    return render(request,"login.html")

def signout(request):

    logout(request)
    return redirect("signin")



def book_event(request,aid):
    # form=EventListForm()
    # if request.method=="POST":
        booked_event=EventList.objects.filter(User_name=request.user.username)
        print(booked_event)
        # form=EventListForm(request.POST,request.FILES)
        # if form.is_valid():
        #     form_data=form.save()
        #     form_data.save()
        #     messages.info(request,"Booking Confirmed")
        #     return redirect("home")
        # else:
        #     messages.info(request,"Booking Not Confirmed!")   

        return render(request,"booking.html",{"book_event":booked_event})    

