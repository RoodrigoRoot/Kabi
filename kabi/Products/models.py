from django.db import models

# Create your models here.
    
class Product(models.Model):
    name = models.CharField(verbose_name=("Nombre"), max_length=50)
    price = models.FloatField(verbose_name=("Precio"))
    active = models.BooleanField(verbose_name=("Disponibilidad"), default=False)
    description = models.TextField(verbose_name=("Descripción"))
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"