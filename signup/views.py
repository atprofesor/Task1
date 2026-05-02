from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirige al login después de registrarse
    template_name = 'registration/signup.html'  # Crea este template para el formulario

# Create your views here.
