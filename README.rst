Ngram Viewer
============

Ngram viewer for Turkish parlamentery texts

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


For the first time
============
*  Install the ``docker`` ``docker-compose`` https://docs.docker.com/install/#supported-platforms
*  Clone the repo and change the ``query`` branch
*  In current repo directory, run ``docker-compose build`` to load all containers.
*  then ``docker-compose up -d`` to run all containers.
*  then go to ``Importing Corpus`` instuctions. to add all corpus to postresql

If not the first time
=============
*  we think you have already install ``docker`` ``docker-compose`` and imported all corpus 
*  You should just run ``docker-compose up -d`` and you will see in `http://localhost:8000/research/`



Importing Corpus
--------

Presumably your ``TXTs`` and ``Tbmm`` files are in your local repository.(For now)
If we think Docker is working. We run the ``import_corpus.py`` script
(which locates in webapp/corpus/management/commands/import_corpus.py)

import_corpus -tbmm <YOUR TBMM PATH> -txts <YOUR TXTs PATH>

 ``docker-compose run django python manage.py import_corpus  -tbmm ./tbmm -txts ./TXTs/``


Glossary
-----
* Fihrist : Catalog
* Dönem : Term
* Yasama Yılı : Legislative Year
* Cilt : Volume
* Birleşim : Session
* Gündem : Agenda

* Yasama Organı : Parliament Types
* Cumhuriyet Senatosu : Csenate
* Kapalı Oturum :Csession (Closed Session)
* Millet Meclisi :  National Assembly



