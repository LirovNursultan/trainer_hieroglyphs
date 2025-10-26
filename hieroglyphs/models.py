from django.db import models

class Dictionary(models.Model):
    name = models.CharField(max_length=100)  # Название, напр. "HSK6" или "Дни недели"
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Hieroglyph(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='hieroglyphs')
    character = models.CharField(max_length=10)  # Иероглиф, напр. "女"
    transcription = models.CharField(max_length=50)  # Напр. "wǒ"
    translation = models.CharField(max_length=100)  # Напр. "Я"
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)  # Аудио-файл, если учитель даст

    def __str__(self):
        return self.symbol

class Sentence(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='sentences')
    translation = models.CharField(max_length=200)  # Перевод на русский
    # Убрали words TextField, добавили:
    hieroglyphs = models.ManyToManyField(Hieroglyph)  # Слова как ссылки на иероглифы

    def __str__(self):
        return self.translation

def flashcards(request, pk):
    dictionary = get_object_or_404(Dictionary, pk=pk)
    hieroglyphs = dictionary.hieroglyphs.all()  # Или random
    # Логика флэш-карт позже
    return render(request, 'hieroglyphs/flashcards.html', {'dictionary': dictionary, 'hieroglyphs': hieroglyphs})

