from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegisterForm(UserCreationForm):
    class Meta:  # Clase para definir metadatos (opciones adicionales)
        model = Usuario
        fields = ["username", "email", "password1", "password2", "rol"]
