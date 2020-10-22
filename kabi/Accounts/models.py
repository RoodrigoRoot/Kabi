from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Accounts(models.Model):

    user = models.OneToOneField(User, verbose_name=("Perfil"), on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="Teléfono", max_length=10)
    created_ay = models.DateField(auto_now=False, auto_now_add=True)
    direction = models.CharField(verbose_name=("Direccion"), max_length=200)
    
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
