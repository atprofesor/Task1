from django.contrib import admin  # <--- ¡Faltaba esta línea!
from .models import post, Article

# Register your models here.
admin.site.register(post)
admin.site.register(Article)
