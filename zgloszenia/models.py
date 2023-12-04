from django.conf import settings
from django.db import models


class Report(models.Model):
    title = models.TextField(max_length=100)
    opis = models.TextField(max_length=300)
    photo = models.ImageField()
    user = models.ManyToOneRel()



