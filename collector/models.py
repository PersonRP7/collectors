""" Collector Data models """

from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from .utils.date_utils import calculate_one_year_end_of_month, date_today
from .utils.status_utils import get_status_choices


class CollectorData(models.Model):
    """
    Collector data model class.
    This model represents a person subscribed to Collector Data organization.
    """

    class Meta:
        """
        Various restrictions and constants that override default table
        settings.
        """

        constraints = [
            UniqueConstraint(
                Lower("first_name"),
                Lower("last_name").desc(),
                name="first_last_name_unique",
            ),
        ]

        verbose_name = "Collector Data"
        verbose_name_plural = verbose_name
        db_table_comment = verbose_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.status}"

    number = models.BigIntegerField(null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    registration_date = models.DateField(default=date_today)
    expiration_date = models.DateField(default=calculate_one_year_end_of_month)

    collector_status_choices = get_status_choices()
    status = models.CharField(
        max_length=10,
        choices=collector_status_choices._asdict(),
        default=collector_status_choices.Active,
    )

    birthdate = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    place_of_residence = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField()

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
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    add_to_whatsapp = models.BooleanField(default=True)
    print_card = models.BooleanField(default=False)

    note = models.TextField(blank=True, null=True)
