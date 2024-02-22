from django.shortcuts import render

def index(request):
    context = {
        'title': 'главная страница'

    }
    return render(request, 'mainapp/index.html', context=context)

