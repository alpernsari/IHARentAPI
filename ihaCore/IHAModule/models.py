from django.db import models

class IHA(models.Model):

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weight = models.IntegerField()
    category = models.CharField(max_length=50)
