"""
Model for handling user profiles in the application.

This module defines the :class:`lettings.Profile` model, representing user profiles within the
application. Each Profile is linked to a corresponding :class:`User` model instance, creating a
one-to-one relationship between users and their profiles.

Model:
    - Profile: Represents a :class:`User` instance with a favourite_city attribute.

Methods:
    - __str__(): Provides a string representation of the :class:`profile.Profile`, which is the
      username of the associated user.

Usage:
    The Profile model is used to store additional user information beyond what is offered by the
    built-in User model. In this case, :class:`profile.Profile` adds a favourite_city attribute.

:param User: Imports the built-in User model from Django's authentication framework.
:param models: Imports Django's database models module.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): The associated user object.
        favorite_city (str): The user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
