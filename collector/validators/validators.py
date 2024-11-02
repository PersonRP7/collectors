""" A collection of custom data validators """

from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import ngettext_lazy


@deconstructible
class EqualLengthValidator(BaseValidator):
    """Custom equality length validator.
    This class is used when you want to limit a field to an exact length.
    The behavior is identical as if MinLengthValidator and MaxLengthValidator
    instances are used.
    """

    message = ngettext_lazy(
        "Ensure this value has exactly %(limit_value)d character (it has "
        "%(show_value)d).",
        "Ensure this value has exactly %(limit_value)d characters (it has "
        "%(show_value)d).",
        "limit_value",
    )
    code = "equal_length"

    def compare(self, a: int, b: int) -> bool:
        """
        Compare the field length with the limit value.
        Arguments:
            a(int): Length of input field.
            b(int): Length defined as the limit.
        Returns:
            bool: Whether length of the input field is different than the
                selected limit.
        """
        return a != b

    def clean(self, x):
        """Clean the input field by returning the length of the written
        characters.
        Returns:
            int: Length of the field to clean.
        """
        return len(x)
