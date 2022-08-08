from django.db import models

class principal(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=300, blank=True, null=True)
    celiac = models.BooleanField()

class drink(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    

class dessert(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    celiac = models.BooleanField()


