from django.contrib import admin
from .models import Sequencia


@admin.register(Sequencia)
class SeuqenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'mtr')
    list_display_links = ('cliente',)
