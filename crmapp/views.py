from django.shortcuts import render,redirect,reverse
from . models import Enquiry,customer,Valid
from adminapp.models import Product
import datetime
from . smssender import sendsms
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    prod=Product.objects.filter(avail='true')
    return render(request,"index.html",{"prods":prod})

def aboutus(request):
    return render(request,"aboutus.html")

def registration(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['Gender']
        address=request.POST['Address']
        contactno=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['Confirm']
        regdate=datetime.datetime.today()
        usertype='customer'
        if password == confirm:
            c=customer(name=name,gender=gender,address=address,contactno=contactno,email=email,regdate=regdate)
            c.save()
            lgin=Valid(userid=email,password=password,usertype=usertype)
            lgin.save()
            return render(request,"registration.html",{"msg":"Registration successfully."})
        else:
            return render(request,"registration.html",{"msg":"Password and Confirm password does not match."})

    return render(request,"registration.html")

def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        contactno=request.POST['number']
        email=request.POST['email']
        subject=request.POST['sub']
        message=request.POST['address']
        posteddate=datetime.datetime.today()
        E=Enquiry(name=name,contactno=contactno,email=email,subject=subject,message=message,posteddate=posteddate)
        E.save()
        sendsms(contactno)
        return render(request,"contact.html",{"msg":"Enquiry is saved"})

    return render(request,"contact.html")

def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Valid.objects.get(userid=userid,password=password)
            if obj is not None:
                if obj.usertype=="customer":
                    request.session["userid"]=userid
                    return redirect(reverse("customerapp:customerhome"))
                elif obj.usertype=="admin":
                    request.session["adminid"]=userid
                    return redirect(reverse("adminapp:adminhome"))
                
        except ObjectDoesNotExist:
            msg="Invalid user"
        return render(request,"login.html",{"msg":msg})
    return render(request,"login.html")