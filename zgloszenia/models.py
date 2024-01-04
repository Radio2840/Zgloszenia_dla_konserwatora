
from django.db import models


class Report(models.Model):
    STATUS_CHOICES = [
        ('not_done', 'Not Done'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    IMPORTANCE_CHOICES = [
        (1, 'Niska'),
        (2, 'Średnia'),
        (3, 'Wysoka'),
    ]
    
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=250)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    status_of_the_report = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_done')
    importance_of_the_report = models.IntegerField(choices=IMPORTANCE_CHOICES, default=1)

    def __str__(self):
        return self.title



