from django.contrib import admin
from .models import Motoristas
@admin.register(Motoristas)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('id_multidev', 'nome', 'cpf')
    list_display_links = ('nome',)
