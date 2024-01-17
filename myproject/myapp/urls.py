# myapp/urls.py
from django.urls import path
from .views import text_input_view

urlpatterns = [
    path('text_input/', text_input_view, name='text_input'),
]
