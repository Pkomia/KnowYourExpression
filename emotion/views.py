from django.shortcuts import render
from django.http import HttpResponse

# import our Ml module here

import test

# Create your views here.
 

def index(request):
   return render(request, 'index.html')

def feature(request):
    return render(request, 'feature.html')

def about(request):
   return render(request, 'about.html')

# def emotion(request):

def check(request):
    status = request.GET.get('Onn', 'off')
    statusoff= request.GET.get('Off', 'off')
    if statusoff == 'Cancle':
        return render(request, 'index.html')
    elif status =='Check':
        # test.model()
        return render(request, 'index.html')
        # print(status)
    else:
        # print(status)
        return render(request, 'index.html')

