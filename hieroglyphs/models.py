from django.db import models

class Dictionary(models.Model):
    name = models.CharField(max_length=100)  # Название, напр. "HSK6" или "Дни недели"
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Hieroglyph(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='hieroglyphs')
    symbol = models.CharField(max_length=10)  # Иероглиф, напр. "女"
    transcription = models.CharField(max_length=50)  # Напр. "wǒ"
    translation = models.CharField(max_length=100)  # Напр. "Я"
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)  # Аудио-файл, если учитель даст

    def __str__(self):
        return self.symbol

class Sentence(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='sentences')
    translation = models.CharField(max_length=200)  # Перевод на русский
    words = models.TextField()  # Слова через запятую, напр. "女,我,的" для разброса

    def __str__(self):
        return self.translation