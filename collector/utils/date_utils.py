""" Utilities module for date manipulation """

from datetime import date, timedelta
import calendar


def calculate_one_year_end_of_month() -> date:
    """
    Calculate the last day of the month that occurs one year from the current date.

    This function calculates the end of the month date 
    from the date that is 365 days from the current date,
    which can be used as a default value for date fields in Django models.

    Returns:
        one_year_later: A `date` object representing the last day of the month
        one year from today.
    """
    target_date = date.today() + timedelta(days=365)
    one_year_later = target_date.replace(
        day=calendar.monthrange(
            target_date.year,target_date.month
        )[1]
    )
    return one_year_later


def date_today() -> date:
    """
    Returns the today's date.

    Returns:
        date: A date object representing today's date.
    """
    return date.today()
