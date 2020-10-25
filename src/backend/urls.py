
from django.contrib import admin
from django.urls import path ,include  
from home.views import *
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',about,name='about'),
    path('services',services,name='services'),
    path('account',account,name='account'),
    path('BLOG',BLOG,name='BLOG'),
    path('coming_soon',coming_soon,name='coming_soon'),
    path('error',error,name='error'),
    path('main',main,name='main'),
    path('',main),
    path('price',price,name='price'),
    path('portfolio',portfolio,name='portfolio'),
    path('services',services,name='services'),
    path('contact',contact,name='contact'),
    
    path('login',login,name="login"),
    path('logout',logout,name="logout"),
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
