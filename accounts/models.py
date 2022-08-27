
from django.db import models
from datetime import datetime

# Create datebase records here.


class Account(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    account_date = models.DateTimeField(default=datetime.now, blank=True)
    account_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
