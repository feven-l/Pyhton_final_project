from django.shortcuts import render
from apps.login_app.models import User, UserManager
from .models import Ing, Drink, Amount
import random

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


def infopage(request):
    return render(request, 'drink_app/drink.html')

def suggest(request):
    drinks = Drink.objects.all()
    random_item = random.choice(drinks)
    context={
        'drink':random_item
    }
    return render(request, 'drink_app/suggest.html', context)
