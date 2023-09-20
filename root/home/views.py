from django.shortcuts import render, redirect
from .forms import ResponseForm
from .models import Response
from django.contrib.auth import logout                  # блок користувача клас ХАКЕР
from django.core.paginator import Paginator



def index(request):
    return render(request, 'home/index.html', {
        'title': 'Головна',
        'page': 'index',
        'app': 'home'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'title': 'Контакти',
        'page': 'contacts',
        'app': 'home'
    })


def feedback_site(request):
    if request.method == 'GET':
        return render(request, 'home/about.html', {
            'title': "Відгук на сайт",
            'page': 'contacts',
            'app': 'about'

        })
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        subject = request.POST.get('subject ', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Отримання адреси електронної пошти, на яку треба відправити повідомлення
        to_email = 'your_email@example.com'

        # Відправка повідомлення
        send_mail('Відгук з сайту', f'Name: {name}\nSubject: {subject}\nEmail: {email}\nMessage: {message}', email,
                  [to_email])
        return HttpResponse('Спасибі за ваш відгук!')

    return render(request, 'home/about.html', {
            'title': "Відгук на сайт",
            'page': 'contacts',
            'app': 'about'
    })


def about(request):
    transit_data = dict()
    transit_data['title'] = ' ПРо нас'
    all_response = Response.objects.all()
    responses_reversed = list(reversed(all_response))
    rows_count = len(responses_reversed)

    paginator = Paginator(responses_reversed, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/about.html', {
        'title': ' ПРо нас',
        'all_response': all_response,
        'rows_count': rows_count,
        'page_obj': page_obj,
    })



def response_create(request):
    transit_data = dict()
    transit_data['title'] = 'Додати відгук на сайт'
    if request.method == 'GET':
        transit_data['form'] = ResponseForm()
        return render(request, 'home/response_create.html', context=transit_data)
    elif request.method == 'POST':
        filled_form = ResponseForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/about')


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html', {
        'title': 'Політика Конфіденційності',
        'page': 'privacy_policy',
        'app': 'home'
    })


def public_contract(request):
    return render(request, 'home/public_contract.html', {
        'title': 'Публічний Договір',
        'page': 'public_contract',
        'app': 'home'
    })


def your_view(request):
    rows_count2 = Response.objects.count()
    return render(request, 'templates/_fragments/Patient Area Starts.html', {'rows_count2': rows_count2})