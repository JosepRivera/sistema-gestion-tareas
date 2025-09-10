from django.urls import path
from .views import registro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registro/", registro, name="registro"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),  # name sirve para referenciar la url en los templates
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"
    ),  # next_page redirige a login tras cerrar sesión
]
