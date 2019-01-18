Research
============
For building

 ``docker-compose up --build``
then if successfully run this command, we can stop the code to run in background.
 ``docker-compose up -d``
when this command runs normal, you can go to 
http://localhost:8000/research

You will see ``simple query`` ``advanced query`` ``simple word2vec`` ``advanced word2vec`` parts. 
``simple query``  The system is looking for a word to contains or not in a text.
``advanced query``  The system is looking for a word to contains or not in a text. But you can filter with document type and parliement type.

Document type  consist of 
    SESSION
    
    CATALOG
    
    AGENDA
    
Parliament type consist of
    CSENATE (Cumhuriyet Senatosu)
    
    CSESSION (Kapalı Oturum)
    
    CA (constituent_assembly_corpus)(Kurucu Meclis)
    
    MGK (Milli Güvenlik Kurulu)
    
    NA national assembly (Millet Meclisi)
    
    TBT (Tbmm birleşik Toplantı)
    
    TBMM 



``simple word2vec`` trains only ``Catalog-Fihrist`` , not all corpus. It fetch the similiar words.

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




