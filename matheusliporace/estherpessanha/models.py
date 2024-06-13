from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    prep_time = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name
