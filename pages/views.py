from django.views.generic import ListView, DetailView   
from .models import post  # <--- Agrega esta línea
from .models import Article  # Cambiamos post por Article

class HomePageView(ListView):
    template_name = "home.html"
    model = post  # Ahora Python ya sabe qué es "post"

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"  # Puedes crear un nuevo HTML
    context_object_name = "articles"     # Nombre personalizado para el HTML
    ordering = ['-published_date']       # Para que los más nuevos salgan arriba

class ArticleDetailView(DetailView): # <--- Esta es la nueva clase
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article" # Nombre que usaremos en el nuevo HTML