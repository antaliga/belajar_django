from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def index(request):
#    return HttpResponse("Hello World")

def index(request):
    my_dict = {'insert_me':"Hai ini halaman ku dari django"}
    return render(request, 'index.html',context=my_dict)