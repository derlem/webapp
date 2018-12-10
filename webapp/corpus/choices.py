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
    CSENATE = "csenate"
    CSESSION = "csession"
    CA = "ca"  # constituent_assembly_corpus
    MGK = "mgk"
    NA = 'na'  # national assembly
    TBT = "tbt"
    TBMM = "tbmm"

    CHOICES = (
        (CSENATE, 'csenate'),
        (CSESSION, 'csession'),
        (CA, 'ca'),
        (MGK, 'mgk'),
        (NA, 'na'),
        (TBT, 'tbt'),
        (TBMM, 'tbmm')
    )
