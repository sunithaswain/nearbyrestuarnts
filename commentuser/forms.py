from django import forms
# from django.contrib.auth.models import Category,Subcategory
class User_form(forms.Form):
	name=forms.CharField(max_length=250)
	password=forms.CharField(max_length=250)
	email=forms.CharField(max_length=250)
	userlocationname=forms.CharField(max_length=250)
class Login_form(forms.Form):
	username=forms.CharField(max_length=250)
	password=forms.CharField(max_length=250)
	
class Location_form(forms.Form): 
	address = forms.CharField(max_length=250)
	state = forms.CharField(max_length=250)
	pincode = forms.CharField(max_length=250)
	state = forms.CharField(max_length=250)

class Resturant_form(forms.Form): 
	locationname = forms.CharField(max_length=250)
	comment = forms.CharField(max_length=250)
	like = forms.CharField(max_length=250)
	timing = forms.CharField(max_length=250)
	Resturantname=forms.CharField(max_length=250)

class Comment_form(forms.Form):
	comment_details = forms.CharField(max_length=250)
	timefield = forms.TimeField()