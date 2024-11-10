from django.http import HttpResponse
from django.shortcuts import render
from task1.forms import UserRegister
from .models import Buyer, Game


# Create your views here.
def platform(request):
    return render(request, 'fourth_task\\platform.html')


def games(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fourth_task\\games.html', context)


def cart(request):
    return render(request, 'fourth_task\\cart.html')


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        for user in users:

            if user.name != username and password == repeat_password:
                Buyer.objects.create(name=username, balance=0.0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')

            if user.name == username:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task\\registration_page.html', info)

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task\\registration_page.html', info)



    else:
        return render(request, 'fifth_task\\registration_page.html')
