from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import meettheteam

def index(request):
    obj = place.objects.all()
    obj1 = meettheteam.objects.all()
    return render(request,'index.html',{'res':obj,'res1':obj1})



