from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('periodontology', periodontology),
    path('therapeutic', therapeutic),
    path('orthopedic', orthopedic),
    path('create', create, name='create'),


]
