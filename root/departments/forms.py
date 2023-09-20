from .models import Articles, ResponseSite
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'about', 'email', 'phone', 'message']

        widgets = {
            'title': TextInput(attrs={
                'class': 'single-input',
                'placeholder': "Прізвище та Iм'я"
            }),

            'about': TextInput(attrs={
                'class': 'single-input',
                'placeholder': "Причина Ващого візиту"
            }),

            'email': TextInput(attrs={
                'class': 'single-input',
                'placeholder': "Адреса електронної пошти"
            }),

            'phone': TextInput(attrs={
                'class': 'single-input',
                'placeholder': "Номер телефону"
            }),

            'message': Textarea(attrs={
                'class': "single-textarea",
                'placeholder': "Примітки для лікаря"
            }),


        }


class ResponseSiteForm(ModelForm):
    class Meta:
        model = ResponseSite
        fields = ['title', 'about', 'message']