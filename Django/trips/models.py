from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trip(models.Model):

    """  here we have created a class that inherits Model. 
     Model is a parent class inside models module that tells the basic funtionality of models. """
    
    trip = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
       return self.trip

class Trip_detail(models.Model):
    """Created another model called Trip_details"""
    city_name = models.ForeignKey(Trip, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Trip_details'

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")