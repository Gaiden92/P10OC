from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=65)
    age = models.IntegerField()

    # confidentialité et RGPD
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()

    def __str__(self):
        return self.username
    
class Project(models.Model):
    choices = (
                ("backend", "Backend"), 
                ("frontend", "Frontend"),
                ("ios", "IOS"),
                ("android", "Android"),
            )
    
    created_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=65)
    description = models.TextField(max_length=255)
    project_type = models.CharField(max_length=65, choices=choices)

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return self.name
    

