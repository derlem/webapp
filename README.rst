Research
============
For building
``docker-compose up --build``
then if successfully run this command, we can stop the code to run in background.
`` docker-compose up -d``
when this command runs normal, you can go to 
http://localhost:8000/research

You will see ``simple query`` ``advanced query`` ``simple word2vec`` ``advanced word2vec`` parts. 
``simple query`` 
``simple word2vec`` trains only ``Catalog-Fihrist`` , not all corpus

(The ``session-oturum`` was taking too long and we felt like we had trouble. But it can be tried on the better computer.) 

``advanced word2vec`` is not working yet.



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




