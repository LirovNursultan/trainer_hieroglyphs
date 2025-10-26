from django.contrib import admin
from .models import Dictionary, Hieroglyph, Sentence

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    filter_horizontal = ('hieroglyphs',)  # Удобный выбор ManyToMany в админке

admin.site.register(Dictionary)
admin.site.register(Hieroglyph)