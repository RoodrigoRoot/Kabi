from django.db import models

# Create your models here.
class Comments(models.Model):
    
    message = models.TextField(verbose_name=("Comentarios"))
    phone = models.CharField(verbose_name=("Teléfono"), max_length=10, blank=True, null=True)
    email = models.EmailField(verbose_name=("Email"), max_length=254,  blank=True, null=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{}-{}".format(self.message[:10], self.created_at)
    