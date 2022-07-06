from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.db.models import Q

from .forms import UserModelForm
from tasks_app.forms import TaskModelForm
from tasks_app.models import Task


def home_page(request):
    if request.user.is_authenticated:

        try:
            search_query = request.GET['search']
            print('Search: ', search_query)
        except:
            search_query = ''
        tasks = Task.objects.filter(owner=request.user)
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query),
        )
        context = {
            'tasks': tasks,
            'search_value': search_query
        }
        return render(request, 'users/home.html', context)
    else:
        return redirect('users:login')


def register_page(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect('users:home')
        else:
            messages.success(request, "Formada xatolik bor!")
            return render(request, 'users/register.html', context)

    else:
        form = UserModelForm()

        context = {'form': form}
        return render(request, 'users/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Muvaffaqiyatli login qilindi!')
            return redirect('users:home')
        else:
            messages.error(request, 'Username yoki password xato!')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout ishladi!')
        return redirect('users:home')
