from django.db import models

from webapp.corpus.choices import DocumentTypes, ParliamentTypes


class ParliamentText(models.Model):
    text = models.TextField()
    term = models.IntegerField(null=True)
    legislative_year = models.IntegerField(null=True)
    volume = models.IntegerField(null=True)
    filename = models.CharField(max_length=5, null=True)
    document_type = models.CharField(choices=DocumentTypes.CHOICES)
    session = models.CharField(max_length=3, null=True)
    parliament_type = models.CharField(choices=ParliamentTypes.CHOICES)
