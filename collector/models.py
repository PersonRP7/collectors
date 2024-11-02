from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from datetime import date, timedelta
from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)


class CollectorData(models.Model):
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("first_name"),
                Lower("last_name").desc(),
                name="first_last_name_unique",
            ),
        ]

        verbose_name = "Collector Data"
        verbose_name_plural = verbose_name

    def one_year_from_now() -> date:
        """
        Returns the date exactly one year from today.

        This function calculates a date that is 365 days from the current date,
        which can be used as a default value for date fields in Django models.

        Returns:
            date: A date object representing one year from today.
        """
        return date.today() + timedelta(days=365)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"

    number = models.BigIntegerField(null=True, blank=True)

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    entry_date = models.DateField(default=date.today)
    expiration_date = models.DateField(default=one_year_from_now)

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Expired", "Expired"),
        ("Removed", "Removed"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")

    birthdate = models.DateField()
    place_of_birth = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    place_of_residence = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=10)

    # Personal number with validators
    personal_number = models.CharField(
        blank=True,
        null=True,
        max_length=11,
        validators=[
            RegexValidator(r"^\d+$", "Personal number must contain only digits."),
            MinLengthValidator(11, "Personal number must be exactly 11 digits."),
            MaxLengthValidator(11, "Personal number must be exactly 11 digits."),
        ],
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    whatsapp = models.BooleanField(default=True)
    print_card = models.BooleanField(default=False)

    reminder_count = models.PositiveIntegerField()

    note = models.CharField(max_length=100, blank=True, null=True)
