""" Utilities module for date manipulation """

from datetime import date, timedelta
from django.utils import timezone
import calendar


def one_year_end_of_month() -> date:
    """
    Calculate the last day of the month that occurs one year from the current date.

    This function calculates the end of the month date
    from the date that is 365 days from the current date,
    which can be used as a default value for date fields in Django models.

    Returns:
        one_year_later: A `date` object representing the last day of the month
        one year from today, and timezone-aware.
    """
    target_date = date.today() + timedelta(days=365)
    one_year_later = target_date.replace(
        day=calendar.monthrange(target_date.year, target_date.month)[1]
    )

    # Convert the resulting date to a timezone-aware datetime at midnight
    one_year_later_datetime = timezone.make_aware(
        timezone.datetime.combine(one_year_later, timezone.datetime.min.time())
    )

    # Return the timezone-aware datetime as the date (no time part)
    return one_year_later_datetime.date()


def date_today() -> date:
    """
    Returns the today's date.

    Returns:
        date: A date object representing today's date.
    """
    return date.today()


def days_from_now(days: int) -> date:
    """
    Calculate the date a certain number of days from today.

    Args:
        days (int): The number of days from the current date.

    Returns:
        date: The target date that is `days` from today.
    """
    return timezone.now().date() + timedelta(days=days)
