from __future__ import unicode_literals
from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, null=False)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    polygon = models.CharField(max_length=500, default='POLYGON ((0.0 0.0, 0.0 0.0, 0.0 0.0))')
