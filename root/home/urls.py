from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('contacts', contacts),
    path('response_create', response_create),
    path('privacy_policy', privacy_policy),
    path('your_view', your_view),
    path('public_contract', public_contract),
    path('licens', licens),

]
