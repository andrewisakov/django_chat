import datetime
from django.db import models


# Create your models here.
class Room(models.Model):
    channel_name = models.CharField(max_length=255,
                                    default=str(datetime.datetime.timestamp(
                                        datetime.datetime.now())))  # ascii
    title = models.CharField(max_length=255)  # Название, utf-8
    staff_only = models.BooleanField(default=False)

    def str(self):
        return self.title
