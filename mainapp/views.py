from django.shortcuts import render, redirect, get_object_or_404

from mainapp.forms import CreateRacipe
from mainapp.models import Recipe, Category


def index(request):
    recipes = Recipe.objects.all()


    context = {
        'title': 'Главная страница',
        'recipes': recipes
    }
    return render(request, 'mainapp/index.html', context=context)

def add_recipe(request):
    recipe_form = CreateRacipe()

    if request.method == 'POST':
        recipe_form = CreateRacipe(request.POST, request.FILES)
        if recipe_form.is_valid():
            new_recipe = Recipe(
                title=recipe_form.cleaned_data['title'],
                description=recipe_form.cleaned_data['description'],
                cooking_steps=recipe_form.cleaned_data['cooking_steps'],
                cooking_time=recipe_form.cleaned_data['cooking_time'],
                img=recipe_form.cleaned_data['img'],
                author=recipe_form.cleaned_data['author'],
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
        'recipe': recipe

    }
    return render(request, 'mainapp/read_recipe.html', context)
