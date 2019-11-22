from django.shortcuts import render, HttpResponse, redirect
from .models import Drink, Ing, Amount

# Create your views here.
def index(request):
    return render(request, 'drink_app/index.html')

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