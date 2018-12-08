import os

from django.core.management import BaseCommand

from webapp.corpus.models import ParliamentText


path = ""


class Command(BaseCommand):
    def handle(self, *args, **options):
        for dirpath, dirs, files in os.walk(path):
            for index, filename in enumerate(files):
                fname = os.path.join(dirpath, filename)

                with open(fname, "r", encoding="utf-8") as f:
                    if index % 100 == 0:
                        print("COUNT : " + str(index) + " in 997862 files ||| " + dirpath[46:48] + ". Donem |" + dirpath[50:51] + ". Yil  |" + dirpath[58:61] + ". Cilt ")

                    txt = f.read()
                    term = dirpath[46:48]
                    legislative_year = dirpath[50:51]
                    volume = dirpath[58:61]
                    session = dirpath[61:64]
                    gundem = dirpath[64:67]

                    if session == "fih":
                        document_type = "fihrist"
                    elif gundem:
                        document_type = "gundem"
                    else:
                        document_type ="birlesim"

                    ParliamentText.objects.create(
                        document_type=document_type,
                        text=txt,
                        term=term,
                        legislative_year=legislative_year,
                        volume=volume,
                        session=session,
                        filename=filename[:-4]
                    )
