from django.db import models


class Hotel(models.Model):
    # TODO Сделать поле для фото отелей
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    rate = models.FloatField()
    reviews = models.ForeignKey(
        "Review", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    data = models.CharField(max_length=1000)

    def __str__(self):
        return self.data
