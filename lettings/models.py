"""
This module contains the models for managing addresses and lettings in the application.

There are two models defined in this module: `Address` and `Letting`. The `Address` model
represents a physical address with attributes such as number, street, city, state, zip code,
and country ISO code. The `Letting` model represents a letting (rental) property with a title
and a one-to-one relationship with an `Address`.

Models:
- `Address`: Represents a physical address with various attributes.
- `Letting`: Represents a letting (rental) property with a title and an associated `Address`.

Notes:
- The `Address` model has a custom verbose name plural to display 'addresses' instead of
'addresss' in the admin interface.
- Validators are used to enforce constraints on certain fields (e.g., `MaxValueValidator`
for `number` and `zip_code`, `MinLengthValidator` for `state` and `country_iso_code`).

Usage:
These models can be used to manage address information for letting properties. They can be
accessed and manipulated through Django's ORM and are designed to be used in conjunction with
Django's admin interface or custom views.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address with the following attributes:
    - number (int): The number of the address.
    - street (str): The name of the street.
    - city (str): The name of the city.
    - state (str): The two-letter abbreviation of the state.
    - zip_code (int): The zip code of the address.
    - country_iso_code (str): The three-letter ISO code of the country.

    Methods:
        __str__(): Returns a string representation of the address in the format
        "{number} {street}".
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting in the system.

    Attributes:
        title (str): The title of the letting.
        address (Address): The address of the letting.

    Methods:
        __str__(): Returns a string representation of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
