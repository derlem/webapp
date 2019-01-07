from django.db import models

from webapp.corpus.choices import DocumentTypes, ParliamentTypes


class ParliamentText(models.Model):
    text = models.TextField()
    term = models.IntegerField(null=True)
    legislative_year = models.IntegerField(null=True)
    volume = models.IntegerField(null=True)
    filename = models.CharField(max_length=5, null=True)
    document_type = models.CharField(max_length=16, choices=DocumentTypes.CHOICES)
    session = models.CharField(max_length=3, null=True)
    parliament_type = models.CharField(max_length=16, choices=ParliamentTypes.CHOICES)

    def __str__(self):
        return self.document_type + ': ' + self.parliament_type + " : "

    class Meta:
        indexes = [
            models.Index(fields=['document_type']),
            models.Index(fields=['parliament_type'])
        ]
