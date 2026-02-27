from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    event_date = models.DateField()
    slots = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.location}"
