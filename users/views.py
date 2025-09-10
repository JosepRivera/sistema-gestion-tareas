from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == "POST":
        form = RegisterForm(
            request.POST
        )  # Crea una instancia del formulario con los datos enviados
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, "Usuario registrado correctamente.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(
        request, "users/registro.html", {"form": form}
    )  # Renderiza la plantilla con el formulario


@login_required
def home(request):
    return render(request, "home.html")
