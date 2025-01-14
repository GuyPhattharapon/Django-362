"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from firstApp import views
from django.http import HttpResponse
from quoteApp import views as qa 

# ฟังก์ชันสำหรับหน้าแรก
def home_view(request):
    return HttpResponse("<h1>My First Django APP!</h1>")

urlpatterns = [
    path('', home_view),  # เส้นทางสำหรับ URL หลัก
    path('admin/', admin.site.urls),
    path('hello/', views.display),  # เส้นทางที่คุณมีอยู่
    path('datetime/', views.displayDateTime),
    path('quote/', qa.displayQuote),  # ตรวจสอบการสะกดให้ถูกต้อง
]