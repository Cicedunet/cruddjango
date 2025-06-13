from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse    
from .models import Band


def index(request):
    bands = Band.objects.all()
    return render(request, 'listings/index.html', {'bands': bands})

def contact(request):
    return render(request, 'listings/contacte.html')
def about(request):
    return render(request, 'listings/about.html')
def base(request):
    return render(request, 'listings/base.html')