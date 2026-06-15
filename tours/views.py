from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Ethiopia Tourism Management System!")

def packages(request):
    return HttpResponse("Our Tour Packages will be displayed here.")