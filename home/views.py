from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


def purchase_request(request):
    form = Purchase_Requisition.objects.all
    context = {'form':form}
    return render(request, 'pages/purchase_request.html', context)