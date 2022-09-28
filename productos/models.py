from django.db import models

# Create your models here.
class personas(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    fecha_n = models.DateField()
    email = models.EmailField(max_length=250)
    genero = models.CharField(max_length=20) 

    def __str__(self):
        return str(self.nombre) + " || " + str(self.telefono)
        

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url