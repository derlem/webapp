class DocumentTypes:
    SESSION = "session"
    CATALOG = "catalog"
    AGENDA = "agenda"

    CHOICES = (
        (SESSION, 'session'),
        (CATALOG, 'catalog'),
        (AGENDA, 'agenda')
    )


class ParliamentTypes:
    TBMM = "tbmm"
    CSENATE = "csenate"
    MGK = "mgk"
    CSESSION = "csession"
    TBT = "tbt"
    CA = "ca"

    CHOICES = (
        (TBMM, 'tbmm'),
        (CSENATE, 'csenate'),
        (MGK, 'mgk'),
        (CSESSION, 'csession'),
        (TBT, 'tbt'),
        (CA, 'ca')
    )
