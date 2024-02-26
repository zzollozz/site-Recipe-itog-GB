from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserEditForm
from mainapp.models import Recipe


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


def edit(request):
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST,
                                 request.FILES,
                                 instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
        return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        content = {
            'title': 'Личный кабинет',
            'edit_form': edit_form
        }
        return render(request, 'authapp/edit.html', content)

def user_read_recipes(request):
    recipes = Recipe.objects.filter(author=request.user)

    context = {
        'title': 'мой рецепты',
        'flag': True,
        'recipes': recipes
    }
    return render(request, 'authapp/read_user_recipes.html', context=context)
