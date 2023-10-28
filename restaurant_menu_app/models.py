from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=255, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
