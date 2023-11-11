from django.db import models


class Hotel(models.Model):
    address = models.CharField(max_length=255)
    rate = models.FloatField()
    reviews = models.ForeignKey("Review", on_delete=models.CASCADE, null=True)


class Review(models.Model):
    data = models.CharField(max_length=1000)
