from django.urls import path
from .views import main_menu  # Пока только это, добавишь другие views позже

urlpatterns = [
    path('', main_menu, name='main_menu'),
]