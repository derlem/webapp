import os

from django.core.management import BaseCommand

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
            # self.get_tbmm_corpus(tbmm_path)
            self.get_TXTs_corpus(txts_path)
        else:
            print('ERROR: PLEASE ADD TBMM AND TXTS PATH')
            print('For Example: import_corpus  -tbmm ./tbmm -txts ./TXTs')

    def get_TXTs_corpus(self, path):
        for index, filename in enumerate(path.rglob("*.txt")):
            with open(filename, "r") as file_content:

                print(file_content)
                txt = file_content.read()
                first_parent = filename.parent.name
                second_parent = filename.parent.parent.name
                parliament_types = filename.parent.parent.parent.name
                print('firsy', first_parent)
                print('second', second_parent)
                print('parliament_types', parliament_types)

                if parliament_types == 'mgk':
                    self.get_MGK_corpus(filename, first_parent, index, second_parent)
                elif parliament_types == 'tbt':
                    self.get_tbt_corpus(filename, first_parent, index, second_parent)
                elif parliament_types == 'millet-meclisi':
                    self.get_MM_corpus(filename, first_parent, index, second_parent)
                elif parliament_types=='kurucu-meclis':
                    self.get_KM_corpus(filename, first_parent, index, second_parent)
                elif parliament_types=='kapali-oturum':
                    self.get_Closed_Session_corpus(filename, first_parent, index, second_parent)


    def get_Closed_Session_corpus(self, filename, first_parent, index, second_parent, txt):

        term = int(second_parent[4:6])

        legislative_year = None
        if second_parent[5:8]=='fih':
            document_type = "catalog"
            session = None

        volume = int(second_parent[5:8])
        session = first_parent[8:]
        if session == "fih":
            document_type = "catalog"
            session = None
        elif session.endswith("gnd"):
            document_type = "agenda"
            session = session[:3]
        else:
            document_type = "session"
        ParliamentText.objects.create(
            document_type=document_type,
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            session=session,
            filename=filename.name[:-4]
        )
        if index % 100 == 0:
            print("IN Kapali Oturum CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_KM_corpus(self, filename, first_parent, index, second_parent, txt):

        # for kurucu meclis term = 1 , for milli birlik komitesi term = 2, for temsilciler meclisi term = 3
        if second_parent.startswith("kurucu"):
            term = 1
        elif second_parent.startswith("milli"):
            term = 2
        else:
            term=3
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
            document_type=document_type,
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            session=session,
            filename=filename.name[:-4]
        )
        if index % 100 == 0:
            print("IN Kurucu Meclis CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")

    def get_MGK_corpus(self, filename, first_parent, index, second_parent,txt):

        # for danisma meclisi term = 2 , for mgk term = 1
        if second_parent.startswith("mgk"):
            term=1
        else:
            term=2
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
            document_type=document_type,
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            session=session,
            filename=filename.name[:-4]
        )
        if index % 100 == 0:
            print("IN MGK CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")


    def get_MM_corpus(self, filename, first_parent, index, second_parent,txt):
        term = int(second_parent[4:6])
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
            document_type=document_type,
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            session=session,
            filename=filename.name[:-4]
        )
        if index % 100 == 0:
            print("IN MM CORPUS -> COUNT : " + str(index) + " || " + str(
                term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")


    def get_tbt_corpus(self, filename, first_parent, index, second_parent,txt):
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
            document_type=document_type,
            text=txt,
            term=term,
            legislative_year=legislative_year,
            volume=volume,
            session=session,
            filename=filename.name[:-4]
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
                print(session)
                if session == "fih":
                    document_type = "catalog"
                    session = None
                elif session.endswith("gnd"):
                    document_type = "agenda"
                    session = session[:3]
                else:
                    document_type = "session"

                # ParliamentText.objects.create(
                #     document_type=document_type,
                #     text=txt,
                #     term=term,
                #     legislative_year=legislative_year,
                #     volume=volume,
                #     session=session,
                #     filename=filename.name[:-4]
                # )

                if index % 100 == 0:
                    print("IN TBMM CORPUS -> COUNT : " + str(index) + " in 997862 files ||| " + str(
                        term) + ". Donem |" + str(legislative_year) + ". Yil  |" + str(volume) + ". Cilt ")
