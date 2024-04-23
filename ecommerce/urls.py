"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booksapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    path("ublog/",upload_blog,name="ublog"),
    path("vblog/",blog,name="vblog"),
    path("ubook/",uploadbook,name="ubook"),
    path("vbook/",view_books,name="vbook"),
    path("",home,name="home"),
    path("index/",index,name="index"),
    path("payment/",customer,name="payment"),
    path("search/",search_result,name="search"),
    path("thank/",thank,name="thank"), 
    path("allbooks/",all_books,name="allbooks"), 

 
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
