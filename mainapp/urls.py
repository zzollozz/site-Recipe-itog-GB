from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='home'),
    path('add_recipe/', mainapp.add_recipe, name='add_recipe'),
    path('read_recipe/<int:pk>/', mainapp.read_recipe, name='read_recipe'),
    path('update_recipe/<int:pk>/', mainapp.update_recipe, name='update_recipe'),
    path('delete_recipe/<int:pk>/', mainapp.delete_recipe, name='delete_recipe'),
]