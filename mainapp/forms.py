from django.forms import ModelForm, TextInput, Textarea

from mainapp.models import Category, Recipe


class CreateRacipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_steps', 'cooking_time', 'img', 'author', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание рецепта'
            }),
            'cooking_steps': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Шаги приготовления'
            })
        }
