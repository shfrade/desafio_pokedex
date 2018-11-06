from django.contrib import admin
from .models import Pokemon, Movimento, Habilidade, Elemento

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Movimento)
admin.site.register(Habilidade)
admin.site.register(Elemento)
