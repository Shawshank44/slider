from django.shortcuts import render
from .models  import *
# Create your views here.

def slider(request):
    cards = Carousel.objects.all()
    return render (request,'index.html',{'card':cards})