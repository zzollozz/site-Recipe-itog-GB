from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm


def login(request):
    login_form = UserLoginForm(data=request.POST)


    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:home'))
    context = {
        'form': login_form,
        'title': 'Вход в личный кабинет',
    }
    return render(request, 'authapp/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:home'))

def register(request):
    register_form = UserRegisterForm(request.POST, request.FILES)
    if request.method == 'POST' and register_form.is_valid():
        register_form.save()
        user = auth.authenticate(username=request.POST.get('username'),
                                 password=request.POST.get('password1'),
                                 )
        auth.login(request, user)
        return HttpResponseRedirect(reverse('mainapp:home'))
    else:
        register_form = UserRegisterForm()
    context = {
        'form': register_form,
        'title': 'Регистрация'
    }
    return render(request, 'authapp/register.html', context)
