from django.urls import path
from. import views

urlpatterns = [
    path("",views.home,name="home"),
    path("ssignup",views.ssignup,name="ssignup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("add_event",views.add_event,name="add_event"),
    path("edit_event/<int:aid>",views.edit_event,name="edit_event"),
    path("delete_event/<int:aid>",views.delete_event,name="delete_event"),
    path("book_event/<int:aid>",views.book_event,name="book_event")
    


   
]