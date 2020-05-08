from django.db import models


class Products(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
