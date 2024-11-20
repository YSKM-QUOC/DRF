from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Xin chào, đây là trang chủ của myapp.")

# Create your views here.
