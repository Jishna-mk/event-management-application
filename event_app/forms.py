from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from service_app.models import EventList


class UserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class EventListForm(ModelForm):
    class Meta:
        model=EventList
        fields="__all__"
