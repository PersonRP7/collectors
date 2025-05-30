""" Collector Data models """

from typing import Any
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.core.validators import RegexValidator
from django.forms import ValidationError
from collector.validators import EqualLengthValidator
from collector.utils.date_utils import one_year_end_of_month, date_today
from collector.utils.status_utils import get_status_choices


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

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    entry_date = models.DateField(default=date_today)
    expiration_date = models.DateField(default=one_year_end_of_month)

    collector_status_choices = get_status_choices()
    status = models.CharField(
        max_length=10,
        choices=collector_status_choices._asdict(),
        default=collector_status_choices.Active,
    )

    birth_date = models.DateField()
    place_of_birth = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    place_of_residence = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=10)

    # Personal number with validators
    personal_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        max_length=11,
        validators=[
            RegexValidator(r"^\d+$", "Personal number must contain only digits."),
            EqualLengthValidator(11, "Personal number must be exactly 11 digits."),
        ],
    )

    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    whatsapp = models.BooleanField(default=True)
    print_card = models.BooleanField(default=False)

    reminder_count = models.PositiveIntegerField(default=0)

    note = models.CharField(max_length=100, blank=True, null=True)

    def clean(self) -> None:
        super().clean()
        self.validate_collector_constraints()

    def save(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def validate_collector_constraints(self) -> None:
        """Validate collector constraints.

        Whenever a model is created or updated, these custom validators are
        invoked.

        Raises:
            ValidationError: When a constraint is validated.
        """
        # Implement a custom restriction that expiry date must be
        # greater than the start date
        if self.expiration_date < self.entry_date:
            raise ValidationError(
                {
                    "expiration_date": [
                        "Expiration date must be greater than registration date."
                    ]
                }
            )

        # If birth date is the future date, display a custom message
        if self.birth_date and self.birth_date > date_today():
            raise ValidationError({"birth_date": ["Birth date must be a past date."]})


class ExpiringSoonCollectorData(CollectorData):
    """
    Proxy model for displaying CollectorData entries
    expiring soon.
    """

    class Meta:
        proxy = True
        verbose_name = "Expiring Soon Collector"
        verbose_name_plural = "Expiring Soon Collectors"
