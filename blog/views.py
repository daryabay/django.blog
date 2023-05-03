from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request,'blog/home1.html')

def AboutPage(request):
    return render(request,'blog/about1.html')

def ContactPage(request):
    return render(request,'blog/contact1.html')
