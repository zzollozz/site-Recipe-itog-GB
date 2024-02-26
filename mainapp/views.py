from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from mainapp.forms import CreateRacipeForm
from mainapp.models import Recipe, Category


def index(request):
    recipes = Recipe.objects.all()[:5]
    context = {
        'title': 'Главная страница',
        'recipes': recipes
    }
    return render(request, 'mainapp/index.html', context=context)

def add_recipe(request):
    recipe_form = CreateRacipeForm()

    if request.method == 'POST':
        recipe_form = CreateRacipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            new_recipe = Recipe(
                title=recipe_form.cleaned_data['title'],
                description=recipe_form.cleaned_data['description'],
                cooking_steps=recipe_form.cleaned_data['cooking_steps'],
                cooking_time=recipe_form.cleaned_data['cooking_time'],
                img=recipe_form.cleaned_data['img'],
                author=request.user,
            )

            new_recipe.save()
            new_recipe.category.add(recipe_form.cleaned_data['category'].values()[0].get('id'))
        return redirect('mainapp:home')

    context = {
        'title': 'Добавление рецепта',
        'form': recipe_form,
    }
    return render(request, 'mainapp/add_recipe.html', context)


def read_recipe(request, pk: int):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {
        'title': 'Рецепт название',
        'cooking_steps_list': recipe.cooking_steps.split('\r'),
        'recipe': recipe

    }
    return render(request, 'mainapp/read_recipe.html', context)


def update_recipe(request, pk: int):
    update_item = get_object_or_404(Recipe, pk=pk)
    data_for_form = {
        'title': update_item.title,
        'description': update_item.description,
        'cooking_steps': update_item.cooking_steps,
        'cooking_time': update_item.cooking_time,
        'img': update_item.img,
        'author': request.user,
        # 'category': update_item.category,
        'is_active': update_item.is_active,
    }
    update_recipe_form = CreateRacipeForm(initial=data_for_form)

    if request.method == 'POST':

        if CreateRacipeForm(request.POST, request.FILES).is_valid():
            update_item.title = request.POST.get('title')
            update_item.description = request.POST.get('description')
            update_item.cooking_steps = request.POST.get('cooking_steps')
            update_item.cooking_time = request.POST.get('cooking_time')
            update_item.img = request.POST.get('img')

            update_item.save()
            return redirect('mainapp:home')

    context = {
        'title': 'Рецепт редактирование',
        'form': update_recipe_form
    }
    return render(request, 'mainapp/update_recipe.html', context)


def delete_recipe(request, pk: int):
    _ = get_object_or_404(Recipe, pk=pk)
    _.delete()
    return HttpResponseRedirect(reverse('authapp:edit'))
