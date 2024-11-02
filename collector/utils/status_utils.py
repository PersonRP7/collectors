""" Utilities module for status manipulation """

from collections import namedtuple

StatusChoices = namedtuple("StatusChoices", ["Active", "Expired", "Removed"])
collector_status_choices = StatusChoices("Active", "Expired", "Removed")


def get_status_choices() -> StatusChoices:
    """
    Get all status choices defined for the user.

    Returns:
        StatusChoices: A class representing possible statuses.
    """
    return collector_status_choices
