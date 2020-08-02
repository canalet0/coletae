from django.db import models

class CollectionPoint(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    addressComplement = models.CharField(max_length=255, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    items = models.CharField(max_length=255, blank=True, null=True)