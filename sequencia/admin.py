from django.contrib import admin
from .models import Sequencia
<<<<<<< Updated upstream
admin.site.register(Sequencia)


#teste
=======

@admin.register(Sequencia)
class SeuqenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'mtr')
    list_display_links = ('cliente',)
>>>>>>> Stashed changes
