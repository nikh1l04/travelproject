from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import meettheteam

def index(request):
    obj = place.objects.all()
    obj1 = meettheteam.objects.all()
    return render(request,'index.html',{'res':obj,'res1':obj1})



# def asdm(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     addn= x+y
#     subn = x-y
#     muln = x*y
#     divn = x/y
#     return render(request,'result.html',{'add':addn,'sub':subn,'multiply':muln,'division':divn})
