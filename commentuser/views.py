from django.shortcuts import render
from .forms import Comment_form
# Create your views here.
import xml.etree.ElementTree as ET
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from .forms import User_form,Login_form,Comment_form
from django.contrib.auth import authenticate
#from django.views import View
import json
from django.views.generic import TemplateView
from django.http import HttpResponse
# from .forms import Team_form
from commentuser.models import User,Location,Resturant,Comment
from django.contrib import messages
from django.contrib.auth.hashers import ( check_password, is_password_usable, make_password,)
def signupdetails(request):
    user_data=mail_data=pwd_data=""
    success_message=""
    if request.method == 'POST':
        #print (request.method,"helloaaaaaa")
        form=User_form(request.POST)
        #print ("coming")
        if form.is_valid():
            print ("hi")
            user_data=request.POST.get("name")
            mail_data=request.POST.get("email")
            pwd_data=request.POST.get("password")
            locationdata=request.POST.get("userlocationname")
            #print (user_data,mail_data,pwd_data)
            pwd = make_password(pwd_data)
            exit_user=User.objects.filter(email=mail_data)
            if exit_user: 
                success_message="User is successfully created"
                return render(request, 'signup.html', {'form':form,'newexist':success_message})
            else:
                 createuser=User.objects.create(name=user_data,password=pwd_data,email=mail_data,userlocationname_id=locationdata)
                 #print (createuser)
        return HttpResponseRedirect('/app/login')
    else:
        print ("afterelse")
        form= User_form()
    return render(request,'signup.html',{'form':form})
def sampledata(request):
    insertuser=User.objects.create(name="namitha",password="Swain@1994",email="namithaswain20@gmail.com",userlocationname_id=1)
    return HttpResponse("user created")
def loginup(request):
    error=""
    useriddata=""
    error_message=""
    if request.method =="POST":
        form = Login_form(request.POST)
        use_name=request.POST.get("username")
        pwd_name=request.POST.get("password")       
        if form.is_valid():            
            user=authenticate(name=use_name,password=pwd_name)
            #auth_login(request, user)
            #print(use_name,pwd_name,"LLLLL")
            user_id = User.objects.filter(name=use_name)
            for i in user_id:
                useriddata=i.id
                #print (useriddata,"}}}}}}")
                # login(request, user)
                return HttpResponseRedirect('/app/location/'+str(useriddata))
        else:
            error_message = "User Not found"
            #print ("User not found")
    else:
        #print ("hello")
        form=Login_form()
    return render(request,'login.html',{'newform':form,'error_message':error_message}) 
def logout(request):
    print("hi")    
    return render(request,'logout.html',{}) 
def locationdetails(request,useriddata):
    #print ("loadtaa")
    iddata=""
    userdata=""
    locid=""
    ad =""
    restdata=""
    #print (useriddata,"SSSSSSSSSS")
    if request.method =="GET":
        #print (request.GET,">>>>>>>>>>>>>")       
        userdata=User.objects.filter(id=useriddata)
        for i in userdata:
            name=i.name
            locid=i.userlocationname_id 
            #print (locid,"{{{{{{{{")
        locationdata=Location.objects.filter(id=locid)
        for loc in locationdata:
            ad =loc.address
            #print (ad,"aaa")
        restuatdata=Resturant.objects.filter(locationname=locid)
        #print (restuatdata,"rrrrrrr")
        # for res in restuatdata:
        #     resname=res.Resturantname
            #print (resname,"pppppppppp")
    return render (request,"location.html",{'form':locationdata,'form1':restuatdata})
def indivualrest(request,useriddata):
    fetchcomment ="" 
    restid=Resturant.objects.filter(locationname=useriddata)
    #fetchcomment=Comment.objects.filter(resturant=useriddata)
    print (restid,"ssssssssssssss")
    if request.method=="POST":
        getcomment = request.POST.get("comment_details")
        print (getcomment,"LLLLLLLLLLLL")
        addcomment=Comment.objects.create(comment_details=getcomment)
    else:
        fetchcomment=Comment.objects.filter(comment_details=useriddata)
        print (fetchcomment,"((((((((((((((((((((((((((((((")
        
    return render (request,"indiviualrestuarnt.html",{'form3':restid,'form4':fetchcomment})  