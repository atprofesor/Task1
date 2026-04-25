from django.views.generic import ListView
from .models import post  # <--- Agrega esta línea

class HomePageView(ListView):
    template_name = "home.html"
    model = post  # Ahora Python ya sabe qué es "post"