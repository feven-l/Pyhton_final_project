from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Drink, Amount, Ing
import re, bcrypt

# Create your views here.
def index(request):
    return render(request, 'drink_app/index.html')

def infopage(request):
	# u = User.objects.get(id=request.session["userid"])
    
    context = {
        "drinks" : Drink.objects.all(),
    }
    return render(request, 'drink_app/drink.html',context)