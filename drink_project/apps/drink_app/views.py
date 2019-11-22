<<<<<<< HEAD
from django.shortcuts import render, HttpResponse, redirect
from .models import Drink, Ing, Amount
=======
from django.shortcuts import render
from apps.login_app.models import User, UserManager
from .models import Ing, Drink, Amount
import random
>>>>>>> d23e6a5aa2c5d24b7f1ccdbc1d80f73f90741f45

# Create your views here.
def index(request):
    print(request.session.keys())
    if 'userid' not in request.session:
        return render(request, 'drink_app/index.html')
    else:
        context={
            'user': User.objects.get(id=request.session['userid'])
        }
        return render(request, 'drink_app/index.html', context)

<<<<<<< HEAD
def infopage(request):
    return render(request, 'drink_app/drink.html')



def search(request):
    search_term = request.POST['search']
    
    return redirect(f'/search={search_term}')

def search_results(request, search_term):
    drink_list = Drink.objects.filter(name__icontains=search_term)
    ing_list =Amount.objects.filter(ing= Ing.objects.filter(name__icontains=search_term))
    context = {
        'drinks': drink_list,
        'ings': ing_list,
        'search_term': search_term
    }

    return render(request, 'drink_app/search_results.html', context)

def all_drinks(request):
    context = {
        'drinks': Drink.objects.all(),
        'all_drinks': True
    }
    return render(request, 'drink_app/search_results.html', context)
=======

def infopage(request, id):
    current_id = id
    context={
        'drinks': Drink.objects.get(id=current_id)
    }
    return render(request, 'drink_app/drink.html', context)

def suggest(request):
    drinks = Drink.objects.all()
    random_item = random.choice(drinks)
    context={
        'drink':random_item
    }
    return render(request, 'drink_app/suggest.html', context)

def alldrinks(request):
    context = {
        'drinks': Drink.objects.all()
    }
    return render(request, 'drink_app/alldrinks.html', context)
>>>>>>> d23e6a5aa2c5d24b7f1ccdbc1d80f73f90741f45
