from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    """A class represent a User

    Arguments:
        AbstractUser -- class abstractuser

    Returns:
        User
    """

    created_time = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(validators=[MinValueValidator(limit_value=15)])

    # confidentialité et RGPD
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()

    def __str__(self) -> str:
        """Method return the string representation of the object.

        Returns:
            str: the object username
        """
        return self.username
