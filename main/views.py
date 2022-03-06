from django.shortcuts import render, redirect
from .models import Celebrities, Maths, Literature, Film
from .forms import CelebrityForm, MathsForm, LiteratureForm, FilmForm


def index(request):
    tasks = Celebrities.objects.all()
    task2 = Maths.objects.all()
    task3 = Literature.objects.all()
    task4 = Film.objects.all()
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'task': tasks, 'task2': task2, 'task3': task3, 'task4': task4})


def literature(request):
    tasks = Literature.objects.all()
    return render(request, 'main/literature.html',  {'title': 'Литература', 'task': tasks})


def film(request):
    tasks = Film.objects.all()
    return render(request, 'main/film.html', {'title': 'Киноиндустрия', 'task': tasks})


def maths(request):
    tasks = Maths.objects.all()
    return render(request, 'main/maths.html', {'title': 'Математика', 'task': tasks})


def toAdd(request):
    error = ''
    if request.method == 'POST':
        form = CelebrityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неправильной'

    form = CelebrityForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)