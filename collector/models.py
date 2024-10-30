from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class CollectorData(models.Model):

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('first_name'),
                Lower('last_name').desc(),
                name='first_last_name_unique',
            ),
        ]

        verbose_name = "Collector Data"
        verbose_name_plural = verbose_name

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    registration_date = models.DateField()

    registration_expiration = models.DateField()

    date_of_birth = models.DateField()

    place_of_birth = models.CharField(
        max_length=150
    )

    street = models.CharField(
        max_length=150
    )

    personal_id_number = models.PositiveBigIntegerField()

    email = models.EmailField(
        max_length = 254
    )

    phone_number = models.CharField(
        max_length = 20
    )

    add_to_whatsapp = models.BooleanField(
        default = True
    )

    note = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"