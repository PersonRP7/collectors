""" Utilities module for date manipulation """

from datetime import date, timedelta


def date_one_year_from_now() -> date:
    """
    Returns the date exactly one year from today.

    This function calculates a date that is 365 days from the current date,
    which can be used as a default value for date fields in Django models.

    Returns:
        date: A date object representing one year from today.
    """
    return date.today() + timedelta(days=365)


def date_today() -> date:
    """
    Returns the today's date.

    Returns:
        date: A date object representing today's date.
    """
    return date.today()
