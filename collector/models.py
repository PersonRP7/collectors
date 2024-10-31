from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from datetime import date, timedelta

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

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def one_year_from_now() -> date:
        """
        Returns the date exactly one year from today.

        This function calculates a date that is 365 days from the current date, 
        which can be used as a default value for date fields in Django models.

        Returns:
            date: A date object representing one year from today.
        """
        return date.today() + timedelta(days=365)

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    registration_date = models.DateField()

    registration_expiration = models.DateField(
        default = one_year_from_now
    )

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