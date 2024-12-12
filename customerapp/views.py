from django.shortcuts import render,redirect
from crmapp.models import customer,Valid
from django.views.decorators.cache import cache_control
from . models import Response,Orders
from adminapp.models import Product
import datetime
# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def customerhome(request):
    try:
        if request.session['userid']!=None:
            cust=customer.objects.get(email=request.session["userid"])
            prod=Product.objects.filter(avail='true')
            ord=Orders.objects.all().count()
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect('crmapp:login')

def logout(request):
    try:
        del request.session["userid"]
    except KeyError:
        return redirect('crmapp:login')
    return redirect('crmapp:login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def response(request):
    try:
        if request.session["userid"]!=None:
            cust=customer.objects.get(email=request.session["userid"])
            if request.method=="POST":
                name=cust.name
                contactno=cust.contactno
                emailaddress=cust.email
                responsetype=request.POST["responsetype"]
                subject=request.POST["subject"]
                responsetext=request.POST["responsetext"]
                posteddate=datetime.datetime.today()
                res=Response(name=name,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype, subject=subject,responsetext=responsetext,posteddate=posteddate)
                res.save()
                msg="Response is submitted"
               
            return render(request,"response.html",locals()) 
    except KeyError:
        return redirect('crmapp:login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword(request):
    try:
        if request.session['userid']!=None:
            if request.method=="POST":
                cust=Valid.objects.get(userid=request.session['userid'])
                oldpswd=request.POST['oldpswd']
                newpswd=request.POST['newpswd']
                conpswd=request.POST['conpswd']
                if cust.password==oldpswd:
                    if oldpswd==newpswd:
                        msg="Old password and new password are same"
                    else:
                        if newpswd==conpswd:
                            cust.password=newpswd
                            cust.save()
                            msg="password change successfully"
                        else:
                            msg="Confirm password is not matched."
                else:
                    msg="Password is not match"
            return render(request,'changepassword.html',locals())
    except:
        return render('crmapp:login')
            

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    try:
        if request.session['userid']!=None:
            cust=customer.objects.get(email=request.session["userid"])
            if request.method=="POST":
                name=request.POST['name']
                gender=request.POST['gender']
                address=request.POST['address']
                contactno=request.POST['contactno']
                email=request.POST['email']
                customer.objects.filter(email=email).update(name=name,gender=gender,address=address,contactno=contactno)
                return redirect("customerapp:customerhome")
            
            return render(request,"viewprofile.html",locals())
    except KeyError:
        return redirect('crmapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def products(request):
    try:
        if request.session['userid']!=None:
            cust=customer.objects.get(email=request.session["userid"])
            prod=Product.objects.filter(avail='true')
            return render(request,"products.html",locals())
    except KeyError:
        return redirect('crmapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def buy(request,id):
    try:
        if request.session['userid']!=None:
            cust=customer.objects.get(email=request.session["userid"])
            prod=Product.objects.get(id=id)
            productname=prod.productname
            price=prod.price
            name=cust.name
            contactno=cust.contactno
            emailaddress=cust.email
            buydate=datetime.datetime.today()
            ord=Orders(productname=productname,price=price,name=name,contactno=contactno,emailaddress=emailaddress,buydate=buydate)
            ord.save()
            Product.objects.filter(id=id).update(avail='false')
            return redirect('customerapp:vieworders')
    except KeyError:
        return redirect('crmapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def vieworders(request):
    try:
        if request.session['userid']!=None:
            cust=customer.objects.get(email=request.session["userid"])
            ord=Orders.objects.filter(emailaddress=cust.email)
            return render(request,"vieworders.html",locals())
    except KeyError:
        return redirect('crmapp:login')