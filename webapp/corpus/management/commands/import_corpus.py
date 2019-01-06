import os

from django.core.management import BaseCommand

from research.query import simpleW2V
from webapp.corpus.models import ParliamentText

from pathlib import Path


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-tbmm', type=str, help='Define a tbmm corpus path')
        parser.add_argument('-txts', type=str, help='Define a TXTs corpus path')

    def handle(self, *args, **kwargs):
        if kwargs['tbmm'] and kwargs['txts']:
            tbmm_path = Path(kwargs['tbmm'])
            txts_path = Path(kwargs['txts'])
            self.get_TXTs_corpus(txts_path)
            self.get_tbmm_corpus(tbmm_path)
        else:
            print('ERROR: PLEASE ADD TBMM AND TXTS PATH')
            print('For Example: import_corpus  -tbmm ./tbmm -txts ./TXTs')

    def get_TXTs_corpus(self, path):
        for index, filename in enumerate(path.rglob("*.txt")):
            with open(filename, "r") as file_content:
                txt = file_content.read()
                first_parent = filename.parent.name
                second_parent = filename.parent.parent.name
                parliament_types = filename.parent.parent.parent.name
                if parliament_types == 'cs':
                    self.get_csenate_corpus(filename, first_parent, index, second_parent, txt)
                elif parliament_types == 'kapali-oturum':
                    self.get_csession_corpus(filename, first_parent, index, txt)
                elif parliament_types == 'kurucu-meclis':
                    self.get_constituent_assembly_corpus(filename, first_parent, index, second_parent, txt)
                elif parliament_types == 'mgk':
                    self.get_MGK_corpus(filename, first_parent, index, second_parent, txt)
                elif parliament_types == 'millet-meclisi':
                    self.get_national_assembly_corpus(filename, first_parent, index, second_parent, txt)
                elif parliament_types == 'tbt':
                    self.get_tbt_corpus(filename, first_parent, index, second_parent, txt)

    def get_csenate_corpus(self, filename, first_parent, index, second_parent, txt):
        term = int(second_parent[5:7])
        legislative_year = None
        volume = int(second_parent[6:9])
        session = first_parent[9:]
        if session == "fih":
            document_type = "catalog"
            session = None
        elif session.endswith("gnd"):
            document_type = "agenda"
            session = session[:3]
        else:
            document_type = "session"
        ParliamentText.objects.create(
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            filename=filename.name[:-4],
            document_type=document_type,
            session=session,
            parliament_type='csenate'
        )
        if index % 100 == 0:
            print("IN C SENATE CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_csession_corpus(self, filename, first_parent, index, txt):


        legislative_year = None

        if first_parent[3:6] == 'fih':
            document_type = "catalog"
            volume = int(first_parent[6:8])
            session = None
            term=None
        else:
            document_type = 'session'
            volume = int(first_parent[5:8])
            session = int(first_parent[-3:])
            term = int(first_parent[3:5])

        ParliamentText.objects.create(
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            filename=filename.name[:-4],
            document_type=document_type,
            session=session,
            parliament_type='csession'
        )

        if index % 100 == 0:
            print("IN CLOSED SESSION CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_constituent_assembly_corpus(self, filename, first_parent, index, second_parent, txt):

        # for kurucu meclis term = 1 , for milli birlik komitesi term = 2, for temsilciler meclisi term = 3
        if second_parent.startswith("kurucu"):
            term = 1
        elif second_parent.startswith("milli"):
            term = 2
        else:
            term = 3
        legislative_year = None
        volume = int(first_parent[6:9])
        session = first_parent[9:]
        if session == "fih":
            document_type = "catalog"
            session = None
        elif session.endswith("gnd"):
            document_type = "agenda"
            session = session[:3]
        else:
            document_type = "session"
        ParliamentText.objects.create(
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            filename=filename.name[:-4],
            document_type=document_type,
            session=session,
            parliament_type='ca'
        )
        if index % 100 == 0:
            print("IN Kurucu Meclis CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_MGK_corpus(self, filename, first_parent, index, second_parent, txt):

        # for danisma meclisi term = 2 , for mgk term = 1
        if second_parent.startswith("mgk"):
            term = 1
        else:
            term = 2
        legislative_year = None
        volume = int(first_parent[6:9])
        session = first_parent[9:]
        if session == "fih":
            document_type = "catalog"
            session = None
        elif session.endswith("gnd"):
            document_type = "agenda"
            session = session[:3]
        else:
            document_type = "session"
            ParliamentText.objects.create(
                text=txt,
                term=term,
                legislative_year=legislative_year,
                volume=volume,
                filename=filename.name[:-4],
                document_type=document_type,
                session=session,
                parliament_type='mgk'
            )
        if index % 100 == 0:
            print("IN MGK CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_national_assembly_corpus(self, filename, first_parent, index, second_parent, txt):
        term = int(second_parent[4:6])
        legislative_year = None
        volume = int(first_parent[6:9])
        session = first_parent[9:]
        if session == "fih":
            document_type = "catalog"
            session = None
        elif session.endswith("gnd"):
            document_type = "agenda"
            session = session[:3]
        else:
            document_type = "session"
        ParliamentText.objects.create(
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            filename=filename.name[:-4],
            document_type=document_type,
            session=session,
            parliament_type='na'

        )
        if index % 100 == 0:
            print("IN MM CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_tbt_corpus(self, filename, first_parent, index, second_parent, txt):
        term = None
        legislative_year = int(second_parent[6:8])
        volume = int(first_parent[6:9])
        session = first_parent[9:]
        if session == "fih":
            document_type = "catalog"
            session = None
        elif session.endswith("gnd"):
            document_type = "agenda"
            session = session[:3]
        else:
            document_type = "session"
        ParliamentText.objects.create(
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            filename=filename.name[:-4],
            document_type=document_type,
            session=session,
            parliament_type='tbt'
        )
        if index % 100 == 0:
            print("IN TBT CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_tbmm_corpus(self, path):
        for index, filename in enumerate(path.rglob("*.txt")):
            with open(filename, "r") as file_content:

                txt = file_content.read()
                first_parent = filename.parent.name
                second_parent = filename.parent.parent.name
                term = int(second_parent[1:3])
                legislative_year = int(second_parent[5:6])
                volume = int(first_parent[6:9])
                session = first_parent[9:]
                if session == "fih":
                    document_type = "catalog"
                    session = None
                elif session.endswith("gnd"):
                    document_type = "agenda"
                    session = session[:3]
                else:
                    document_type = "session"

                ParliamentText.objects.create(
                    text=txt,
                    term=term,
                    legislative_year=legislative_year,
                    volume=volume,
                    filename=filename.name[:-4],
                    document_type=document_type,
                    session=session,
                    parliament_type='tbmm'
                )

                if index % 100 == 0:
                    print("IN TBMM CORPUS -> COUNT : " + str(index) + " in 997862 files ||| " + str(
                        term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")
