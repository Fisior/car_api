from django.db import models


class Car(models.Model):
    ENGINE = [
        ('PB', 'Petrol'),
        ('ON', 'Diesel'),
        ('HY', 'Hybrid'),
        ('EL', 'Electric'),
    ]
    WHEEL_DRIVE = [
        ('FR', 'Front'),
        ('RE', 'Rear'),
        ('FO', 'Four')
    ]
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    engine = models.CharField(choices=ENGINE, max_length=2)
    wheel_driver = models.CharField(choices=WHEEL_DRIVE, max_length=2)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.brand + ' ' + self.model
