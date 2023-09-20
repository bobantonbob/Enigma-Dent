from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .forms import ResponseSiteForm


def index(request):
    return render(request, 'departments/index.html', {
        'title': 'Послуги',
        'page': 'index',
        'app': 'departments'
    })

def therapeutic(request):
    return render(request, 'departments/therapeutic.html', {
        'title': 'Терапевтична стоматологія',
        'page': 'therapeutic',
        'app': 'departments'
    })

def periodontology(request):
    return render(request, 'departments/periodontology.html', {
        'title': 'Пародонтологічна стоматологія',
        'page': 'periodontology',
        'app': 'departments'
    })

def orthopedic(request):
    return render(request, 'departments/orthopedic.html', {
        'title': 'Ортопедична стоматологія',
        'page': 'orthopedic',
        'app': 'departments'
    })
def create(request):
    transit_data = dict()
    transit_data['title'] = 'ЗАПИС НА ПРИЙОМ ДО ЛІКАРЯ'
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Форма була заповнена з помилками"
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'departments/create.html', data)


def Subscription(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Форма була заповнена з помилками"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request,  data)


def response_site(request):
    form = ResponseSiteForm()

    data = {
        'form': form

    }


    return render(request, '/_fragments/Patient Area Starts.html', data)