from django.db import models

class Url(models.Model):
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address
