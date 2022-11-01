from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class BookedList(models.Model):
    Event_id=models.CharField(max_length=100)
    User_name=models.CharField(max_length=200)
    Event_name=models.CharField(max_length=200)
    Sponser_name=models.CharField(max_length=200)
    Start_date=models.CharField(max_length=10)
    End_date=models.CharField(max_length=10)
    Event_image=models.ImageField(upload_to="events")


    