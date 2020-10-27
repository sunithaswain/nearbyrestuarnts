from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.
class User(models.Model): 
	name = models.CharField(max_length=70, blank=False)
	password = models.CharField(max_length=70, blank=False)
	email=models.CharField(max_length=250,blank=True)
	userlocationname = models.ForeignKey('Location', on_delete=models.CASCADE)

class Location(models.Model): 
	address = models.CharField(max_length=70, blank=False)
	state = models.CharField(max_length=70, blank=False)
	pincode = models.CharField(max_length=70, blank=False)
	state = models.CharField(max_length=70, blank=False)

class Resturant(models.Model): 
	locationname = models.ForeignKey('Location', on_delete=models.CASCADE)
	#comment = models.CharField(max_length=70, blank=False)
	like = models.CharField(max_length=70, blank=False)
	timing = models.CharField(max_length=70, blank=False)
	Resturantname=models.CharField(max_length=70, blank=False)

class Comment(models.Model):
	resturant=models.ForeignKey('Resturant', on_delete=models.CASCADE)
	comment_details=models.CharField(max_length=70, blank=False)
	timefield=models.DateTimeField()  