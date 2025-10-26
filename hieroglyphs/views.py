from django.shortcuts import render, get_object_or_404
from .models import Dictionary, Hieroglyph, Sentence

def main_menu(request):
    dictionaries = Dictionary.objects.all()
    return render(request, 'hieroglyphs/main_menu.html', {'dictionaries': dictionaries})

def dictionary_detail(request, pk):
    dictionary = get_object_or_404(Dictionary, pk=pk)
    hieroglyphs = dictionary.hieroglyphs.all()
    return render(request, 'hieroglyphs/dictionary_detail.html', {'dictionary': dictionary, 'hieroglyphs': hieroglyphs})

def study_menu(request, pk):
    dictionary = get_object_or_404(Dictionary, pk=pk)
    return render(request, 'hieroglyphs/study_menu.html', {'dictionary': dictionary})    

def practice(request, pk):
    dictionary = get_object_or_404(Dictionary, pk=pk)
    hieroglyphs = dictionary.hieroglyphs.all()  # Для генерации вопросов
    # Логика: генерируй вопрос (e.g. random hieroglyph, 4 варианта перевода)
    # Пока заглушка
    return render(request, 'hieroglyphs/practice.html', {'dictionary': dictionary, 'hieroglyphs': hieroglyphs})

def sentence_build(request, pk):
    dictionary = get_object_or_404(Dictionary, pk=pk)
    sentences = dictionary.sentences.all()  # Все предложения
    # Логика: выбери random sentence, разбросай слова
    # Пока заглушка
    return render(request, 'hieroglyphs/sentence_build.html', {'dictionary': dictionary, 'sentences': sentences})