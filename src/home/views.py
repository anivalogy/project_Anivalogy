from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse


from .models import *


def login(request):
    error=""
    if request.method=='POST':
        u=request.POST["uname"]
        p=request.POST["pwd"]
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html', d)


def logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')





































# Create your views here.
def home(request):
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def account(request):
    return render(request,'account.html')

def BLOG(request):
    return render(request,'blog.html')

def coming_soon(request):
    return render(request,'coming_soon.html')

def error(request):
    return render(request,'error.html')





def portfolio(request):
    queryset = Photo.objects.all()
    context = {
    "photos": queryset,
}
    return render(request,'portfolio.html',context)


def price(request):
    return render(request,'price.html')






































































def services(request):
    queryset = Services.objects.all()
    queryset1 = Services_heading.objects.all()
    contnet = {
        "Services": queryset, 'services':queryset1
}
    return render(request, 'services.html',contnet)
































































































































































def main(request):
    queryset = team.objects.all()
    content = {
        "teams": queryset,
    }
    return render(request, 'main.html',content)



def contact(request):
    return render(request,'contact.html')
