from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Accounts(models.Model):

    user = models.OneToOneField(User, verbose_name=("Perfil"), on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="Teléfono", max_length=10)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    direction = models.CharField(verbose_name=("Dirección"), max_length=200)
    
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"


class Company(models.Model):
    name = models.CharField(verbose_name=("Nombre"), max_length=50)
    phone = models.CharField(verbose_name=("Teléfono"), max_length=10)
    direction = models.CharField(verbose_name=("Dirección"), max_length=200)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
