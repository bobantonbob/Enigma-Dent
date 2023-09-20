from django.forms import ModelForm, TextInput, Textarea
from .models import Response
from django.shortcuts import render



class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['name', 'email', 'response', 'image']

        widgets = {
            'name': TextInput(attrs={
                'class': 'single-input',
                'placeholder': "Прізвище та Iм'я"
            }),

            'email': TextInput(attrs={
                'class': 'single-input',
                'placeholder': "Адреса електронної пошти"
            }),

            # 'image': TextInput(attrs={
            #     'class': 'single-input',
            #     'placeholder': "Ваше фото"
            # }),

            'response': Textarea(attrs={
                'class': "single-textarea",
                'placeholder': "Ваш відгуг про нас ;)"
            }),

        }



