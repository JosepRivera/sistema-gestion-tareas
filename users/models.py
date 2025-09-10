from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ROLES = (
        ("lider", "Lider"),
        ("miembro", "Miembro"),
    )
    rol = models.CharField(choices=ROLES, default="miembro")

    def __str__(self):
        return f"{self.username} - {self.rol}"
