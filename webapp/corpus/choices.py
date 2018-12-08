class DocumentTypes:
    TERM = "term"
    CATALOG = "catalog"
    AGENDA = "agenda"

    CHOICES = (
        (TERM, 'Term'),
        (CATALOG, 'Catalog'),
        (AGENDA, 'Agenda')
    )


class ParliamentTypes:
    TBMM = "tbmm"
    CSENATE = "csenate"
    MGK = "mgk"
    CSESSION = "csession"
    TBT = "tbt"
    CA = "ca"

    CHOICES = (
        (TBMM, 'TBMM'),
        (CSENATE, 'csenate'),
        (MGK, 'MGK'),
        (CSESSION, 'csession'),
        (TBT, 'TBT'),
        (CA, 'CA')
    )
