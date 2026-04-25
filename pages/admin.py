from django.contrib import admin  # <--- ¡Faltaba esta línea!
from .models import post

# Register your models here.
admin.site.register(post)
