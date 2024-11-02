""" Utilities module for date manipulation """

from datetime import date, timedelta
import calendar


def date_one_year_from_now() -> date:
    """
    Returns the date exactly one year from today.

    This function calculates the end of the month date from the date that is 365 days from the current date,
    which can be used as a default value for date fields in Django models.

    Returns:
        one_year_later: A date object representing the end of the month one year from today.
    """
    one_year_later = date.today() + timedelta(days=365)
    one_year_later = one_year_later.replace(day=calendar.monthrange(one_year_later.year,one_year_later.month)[1])
    return one_year_later


def date_today() -> date:
    """
    Returns the today's date.

    Returns:
        date: A date object representing today's date.
    """
    return date.today()
