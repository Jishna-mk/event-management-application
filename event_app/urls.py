from django.urls import path
from. import views

urlpatterns = [
    path("",views.first,name="first"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("add_event",views.add_event,name="add_event")
    
]