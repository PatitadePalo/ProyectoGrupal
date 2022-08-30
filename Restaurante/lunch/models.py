from django.db import models

class principal(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=300, blank=True, null=True)
    celiac = models.BooleanField()
    image = models.ImageField(upload_to='lunch/', blank=True, null=True)

    def __str__(self):
        return self.name

class drink(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='lunch/', blank=True, null=True)
    def __str__(self):
        return self.name   

class dessert(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    celiac = models.BooleanField()
    image = models.ImageField(upload_to='lunch/', blank=True, null=True)
    def __str__(self):
        return self.name

