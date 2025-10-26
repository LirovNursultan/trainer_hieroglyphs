from django.shortcuts import render
from .models import Dictionary  # Пока только это, добавишь другие модели позже

def main_menu(request):
    dictionaries = Dictionary.objects.all()
    return render(request, 'hieroglyphs/main_menu.html', {'dictionaries': dictionaries})