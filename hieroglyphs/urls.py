from django.urls import path
from .views import main_menu, dictionary_detail, study_menu, practice, sentence_build

urlpatterns = [
    path('', main_menu, name='main_menu'),
    path('dictionary/<int:pk>/', dictionary_detail, name='dictionary_detail'),
    path('dictionary/<int:pk>/study/', study_menu, name='study_menu'),
    path('dictionary/<int:pk>/practice/', practice, name='practice'),
    path('dictionary/<int:pk>/sentence_build/', sentence_build, name='sentence_build'),
    #path('dictionary/<int:pk>/flashcards/', flashcards, name='flashcards'),
    # Добавь другие позже
]