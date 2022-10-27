from django.urls import path
from .import views
from .models import BookedList

urlpatterns = [
    path("",views.first,name="first"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    
    
    
]