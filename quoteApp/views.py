from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuote(request):  # แก้ชื่อจาก displayQoute เป็น displayQuote
    return HttpResponse("The best investment we can make is in ourselves. - Warren Buffett")  # แก้คำว่า "makes" เป็น "make" และ "ourself" เป็น "ourselves"
