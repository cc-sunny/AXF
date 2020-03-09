from django.http import HttpResponse
from django.shortcuts import render

from app.models import MainWheel


def index(request):
    return HttpResponse('index')


def home(request):
    main_wheels =MainWheel.objects.all()
    date = {
        'title':'首页',
        'main_wheels':main_wheels,
    }
    return render(request,'main/home.html',context=date)


def market(request):
    return render(request,'main/market.html')


def cart(request):
    return render(request,'main/cart.html')


def mine(request):
    return render(request,'main/mine.html')