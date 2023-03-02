from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.description}"