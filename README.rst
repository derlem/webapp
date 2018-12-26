Ngram Viewer
============

Ngram viewer for Turkish parlamentery texts

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT

Importing Corpus
--------

Presumably your `TXTs` and `Tbmm` files are in your local repository.(For now)
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



