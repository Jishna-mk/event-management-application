from asyncio import events
from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from event_app.forms import UserAddForm
from event_app.models import BookedList
from.forms import EventListForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.models import EventList


# Create your views here


def home(request):
    events=EventList.objects.all()
    return render(request, "shome.html",{"events":events})

# service provider signup
def ssignup(request):
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

    return render(request, "sesignup.html", {"form": form})

#service provider login
def signin(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("first")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("signin")

    return render(request,"selogin.html")
#service provider signout
def signout(request):

    logout(request)
    return redirect("signin")

def add_event(request):
    form=EventListForm()
    if request.method=="POST":
        form=EventListForm(request.POST,request.FILES)
        if form.is_valid():
            form_data=form.save()
            form_data.save()
            messages.info(request,"successfully Added")
            return redirect("home")
        else:
            messages.info(request,"Event is not Added")   

    return render(request,"add_event.html",{"Add_form":form})
  
def edit_event(request,aid):
    if request.method=="POST":
        EventList.objects.filter(id=aid).update(Event_name=request.POST["Event_name"],Event_detail=request.POST["Event_detail"],
        Event_venue=request.POST["Event_venue"],Start_date=request.POST["Start_date"],End_date=request.POST["End_date"])
        return redirect("home")
    new_event=EventList.objects.get(id=aid)
    return render(request,"edit_event.html",{"new_event": new_event})  

def delete_event(request,aid):
    Event=EventList.objects.get(id=aid)
    Event.delete()
    messages.info(request,"successfully deleted")
    return redirect("home")

def book_event(request,aid):
    Event=EventList.objects.get(id=aid)
    print(request.session["username"])
    b_instance=BookedList(Event_name=Event.Event_name,Sponser_name=Event.Sponser_name,Start_date=Event.Start_date,End_date=Event.End_date,User_name=request.session["username"])
    b_instance.save()
    return redirect('my_bookings')
        
def my_bookings(request):
    booked_list=BookedList.objects.filter(User_name=request.session["username"])
    return render(request,"booking.html",{"bookedlist":booked_list})
    
