from django.db import models

# Create your models here.
class Location(models.Model):
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longtitude = models.DecimalField(max_digits=9, decimal_places=6)
  description = models.TextField()

  def __str__(self):
    return self.description