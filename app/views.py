from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,ContactForm
from django.contrib.auth import authenticate,login,logout
from . models import Carousel,Menu,Logo,SubMenu



# Create your views here.

def home(request):
    obj=Carousel.objects.all()
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/home.html',{'obj':obj,'item':item,'logo':logo,'sub_item':sub_item})


def about(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/about.html',{'item':item,'logo':logo,'sub_item':sub_item})

def service(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/service.html',{'item':item,'logo':logo,'sub_item':sub_item})

def portfolio(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/portfolio.html',{'item':item,'logo':logo,'sub_item':sub_item})

def team(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/team.html',{'item':item,'logo':logo,'sub_item':sub_item})


def contact(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/contact.html',{'item':item,'logo':logo,'sub_item':sub_item})

def price(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/pricing.html',{'item':item,'logo':logo,'sub_item':sub_item})


def blog(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/blog.html',{'item':item,'logo':logo,'sub_item':sub_item})

def error_page(request):
    return render (request,'app/404.html')

def singlepost(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    return render (request,'app/single-post.html',{'item':item,'logo':logo,'sub_item':sub_item})


def signup(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
           
            form.save()
            return HttpResponseRedirect('/login/')
            
    else:
        form= SignUpForm()
    return render (request,'app/signup.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form= LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user =authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    
                    return HttpResponseRedirect('/')
        else:
            form= LoginForm()
        return render (request,'app/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
    item=Menu.objects.all()
    logo=Logo.objects.all()
    sub_item=SubMenu.objects.all()
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form=ContactForm()
    else:
        form=ContactForm()
    return render (request,'app/contact.html',{'form':form,'item':item,'logo':logo,'sub_item':sub_item})
