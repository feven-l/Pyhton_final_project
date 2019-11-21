from django.shortcuts import render
from apps.login_app.models import User, UserManager
from .models import Ing, Drink, Amount

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

def favorite(request):
    return render(request, 'drink_app/order.html')