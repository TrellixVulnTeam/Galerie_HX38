from django.db import models
import pyperclip
import random

# Create your models here.

class Location(models.Model):
    """
    A class for locations where a Photo were taken
    """
    city = models.CharField(max_length=244)
    country = models.CharField(max_length=244)

    def __str__(self):

        return f"{self.city}, {self.country}"

    def save_location(self):
        """
        A method to save the location
        """
        return self.save()

    @classmethod
    def find_photos_by_location(cls, id):
        return cls.objects.filter(photo__location__id = id)

class Category(models.Model):
    """
    A class for the category the Photo falls under
    """
    name = models.CharField(max_length=144)

    def __str__(self):
        """
        String representation
        """
        return self.name

    def save_category(self):
        """
        A method to save the category name
        """
        return self.save()
