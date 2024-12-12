from django.shortcuts import render,redirect
from crmapp.models import customer,Valid,Enquiry
from customerapp.models import Response,Orders
from django.views.decorators.cache import cache_control
from . models import Product

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust_count=customer.objects.all().count()
            enq_cust=Enquiry.objects.all().count()
            res=Response.objects.filter(responsetype='feedback').count()
            comp=Response.objects.filter(responsetype='complaint').count()
            prd=Product.objects.all().count()
            ord=Orders.objects.all().count()
            return render(request,"adminhome.html",locals())
    except:
        return redirect("crmapp:login")
    
def logout(request):
    try:
        del request.session["adminid"]
        return redirect("crmapp:login")
    except:
        return redirect('crmapp:login')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustomers(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust=customer.objects.all()
            return render(request,"viewcustomers.html",locals())
    except:
        return redirect("crmapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiries(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            enq=Enquiry.objects.all()
            return render(request,"viewenquiries.html",locals())
    except:
        return redirect("crmapp:login")


def delenq(request,id):
    del_enq=Enquiry.objects.get(id=id)
    del_enq.delete()
    return redirect("adminapp:viewenquiries")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedbacks(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            feed=Response.objects.filter(responsetype="feedback")
            return render(request,"viewfeedbacks.html",locals())
    except:
        return redirect("crmapp:login")

def delfeedback(request,id):
    del_feed=Response.objects.get(id=id)
    del_feed.delete()
    return redirect("adminapp:viewfeedbacks")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplains(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            com=Response.objects.filter(responsetype="complaint")
            return render(request,"viewcomplains.html",locals())
    except:
        return redirect("crmapp:login")

def delcomplaint(request,id):
    del_complaint=Response.objects.get(id=id)
    del_complaint.delete()
    return redirect("adminapp:viewcomplains")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminchangepswd(request):
    try:
        if request.session['adminid']!=None:
            if request.method=="POST":
                admin=Valid.objects.get(userid=request.session['adminid'])
                oldpswd=request.POST['oldpswd']
                newpswd=request.POST['newpswd']
                conpswd=request.POST['conpswd']
                if admin.password==oldpswd:
                    if oldpswd==newpswd:
                        msg="Old password and new password are same"
                    else:
                        if newpswd==conpswd:
                            admin.password=newpswd
                            admin.save()
                            msg="password change successfully"
                        else:
                            msg="Confirm password is not matched."
                else:
                    msg="Password is not match"
            return render(request,'adminchangepswd.html',locals())
    except:
        return render('crmapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            if request.method=="POST":
                productname=request.POST['productname']
                mfgdate=request.POST['mfgdate']
                expdate=request.POST['expdate']
                price=request.POST['price']
                productpic=request.FILES['productpic']
                prd=Product(productname=productname,mfgdate=mfgdate,expdate=expdate,price=price,productpic=productpic,avail='true')
                prd.save()
                msg='Product is added'
                return render(request,"product.html",locals())

            return render(request,"product.html",locals())
    except:
        return redirect("crmapp:login")
  
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewproduct(request):
    try:
        if request.session["adminid"]!=None:
            prod=Product.objects.all()
            adminid=request.session["adminid"]
            return render(request,"viewproduct.html",locals())
    except:
        return redirect("crmapp:login")

def delproduct(request,id):
    del_product=Product.objects.get(id=id)
    del_product.delete()
    return redirect("adminapp:viewproduct")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustorders(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            ord=Orders.objects.all()
            return render(request,"viewcustorders.html",locals())
    except:
        return redirect("crmapp:login")