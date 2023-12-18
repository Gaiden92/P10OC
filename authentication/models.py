from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_time = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()

    # confidentialité et RGPD
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()

    def __str__(self) -> str:
        return self.username
