from django.db import models


# Create your models here.

class DocumentTypes:
    TERM = "term"
    CATALOG = "catalog"
    AGENDA = "agenda"

    CHOICES = (
        (TERM, 'term'),
        (CATALOG, 'catalog'),
        (AGENDA, 'agenda')
    )


class ParliamentTypes:
    TBMM = "tbmm"
    CSENATE = "csenate"
    MGK = "mgk"
    CSESSION = 'csession'
    TBT = 'tbt'
    CA = 'ca'

    CHOICES = (
        (TBMM, 'tbmm'),
        (CSENATE, 'csenate'),
        (MGK, 'mgk'),
        (CSESSION, 'csession'),
        (TBT, 'tbt'),
        (CA, 'ca')
    )


class ParliamentText(models.Model):
    text = models.TextField()
    term = models.IntegerField(null=True)
    legislative_year = models.IntegerField(null=True)
    volume = models.IntegerField(null=True)
    filename = models.CharField(max_length=5, null=True)
    document_type = models.CharField(choices=DocumentTypes.CHOICES)
    session = models.CharField(max_length=3, null=True)
    parliament_type = models.CharField(choices=ParliamentTypes.CHOICES)
