from django.http import HttpResponse
from django.shortcuts import render
def ram(request):
    return render(request,'countwords.html')
def count(request):
    mess=request.GET['message']
    wl=mess.split()
    #print(wl)
    return render(request,'count.html',{'msg':mess,'length':len(wl)})