from django.urls import path
from .import views
from .models import BookedList

urlpatterns = [
    path("",views.first,name="first"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("book_event/<int:aid>",views.book_event,name="book_event"),
    path("cancel_event/<int:aid>",views.cancel_event,name="cancel_event")
    
]