import os

from django.core.management import BaseCommand

from webapp.corpus.models import ParliamentText

from pathlib import Path


path = Path("/app/data")


class Command(BaseCommand):
    def handle(self, *args, **options):
        files = path.rglob("*.txt")

        for index, filename in enumerate(files):
            with open(filename, "r") as file_content:
                if index % 100 == 0:
                    # print("COUNT : " + str(index) + " in 997862 files ||| " + dirpath[46:48] + ". Donem |" + dirpath[50:51] + ". Yil  |" + dirpath[58:61] + ". Cilt ")
                    pass

                txt = file_content.read()

                first_parent = filename.parent.name
                second_parent = filename.parent.parent.name

                term = int(second_parent[1:3])
                legislative_year = int(second_parent[5:6])
                volume = int(first_parent[6:9])
                session = first_parent[9:]

                if session == "fih":
                    document_type = "fihrist"
                    session = None
                elif session.endswith("gnd"):
                    document_type = "gundem"
                    session = session[:3]
                else:
                    document_type ="birlesim"

                ParliamentText.objects.create(
                    document_type=document_type,
                    text=txt,
                    term=term,
                    legislative_year=legislative_year,
                    volume=volume,
                    session=session,
                    filename=filename.name[:-4]
                )
