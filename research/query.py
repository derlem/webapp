import gensim
from django.db.models import Case, When
from gensim.test.utils import common_texts, get_tmpfile

from research.serializers import *
import logging

from webapp.corpus.models import ParliamentText
import time

log = logging.getLogger(__name__)


def simpleQuery(query):
    start_time = time.time()

    txt_search_input = query['txt_search_input']

    q = ParliamentText.objects.filter(text__icontains=txt_search_input)
    q.filter(document_type='session')
    data = {}
    data['term'] = []
    for i in range(1, 26):
        data['term'].append(q.filter(term=(i)).count())

    print("---Finished !!!  %s seconds ---" % (time.time() - start_time))
    duration = time.time() - start_time

    ser = SimpleSerializer(
        context={"type": "simple", "query_string": txt_search_input.__str__(), "duration": duration.__str__(),
                 "payload": data['term'].__str__()})

    log.info(q.query.__str__())
    log.info(ser.context.__str__())
    return ser.context


# query=>  <QueryDict: {'csrfmiddlewaretoken': ['UrhBQ36u8TBdRNxWvm2sCqFuWH6Fkkxxuac1Zstc6FUwri4SfV9NZQqF5gkz1FP5'],
# 'txt_search_input': [''], 'txt_advanced_search_input': ['deneme'], 'chk_session': ['on'],
#  'chk_catalog': ['on'], 'chk_agenda': ['on'], 'chk_tbmm': ['on'], 'chk_csenate': ['on'],
#  'chk_csession': ['on'], 'chk_ca': ['on'], 'chk_mgk': ['on'], 'chk_na': ['on'], 'chk_tbt': ['on']}>
def advancedQuery(query):
    # print(query)
    txt_advanced_search_input = query['txt_advanced_search_input']
    start_time = time.time()

    q = ParliamentText.objects.filter(text__contains=txt_advanced_search_input)

    # DOCUMENT TYPE
    session_filter = ParliamentText.objects.none()
    catalog_filter = ParliamentText.objects.none()
    agenda_filter = ParliamentText.objects.none()
    if ('chk_session' in query):
        session_filter = q.filter(document_type='session')
    if ("chk_catalog" in query):
        catalog_filter = q.filter(document_type='catalog')
    if ("chk_agenda" in query):
        agenda_filter = q.filter(document_type='agenda')
    q = session_filter | catalog_filter | agenda_filter

    tbmm_filter = ParliamentText.objects.none()
    csenate_filter = ParliamentText.objects.none()
    csession_filter = ParliamentText.objects.none()
    ca_filter = ParliamentText.objects.none()
    mgk_filter = ParliamentText.objects.none()
    na_filter = ParliamentText.objects.none()
    tbt_filter = ParliamentText.objects.none()

    # PARLIAMENT TYPE
    if ("chk_tbmm" in query):
        tbmm_filter = q.filter(parliament_type='tbmm')
    if ("chk_csenate" in query):
        csenate_filter = q.filter(parliament_type='csenate')
    if ("chk_csession" in query):
        csession_filter = q.filter(parliament_type='csession')
    if ("chk_ca" in query):
        ca_filter = q.filter(parliament_type='ca')
    if ("chk_mgk" in query):
        mgk_filter = q.filter(parliament_type='mgk')
    if ("chk_na" in query):
        na_filter = q.filter(parliament_type='na')
    if ("chk_tbt" in query):
        tbt_filter = q.filter(parliament_type='tbt')
    q = tbmm_filter | csenate_filter | csession_filter | ca_filter | mgk_filter | na_filter | tbt_filter
    data = {}
    data['term'] = []
    for i in range(1, 2):
        data['term'].append(q.filter(term=(i)).count())

    print("---Finished !!!  %s seconds ---" % (time.time() - start_time))
    duration = time.time() - start_time

    ser = SimpleSerializer(
        context={"type": "advanced", "query_string": txt_advanced_search_input.__str__(),
                 "duration": duration.__str__(),
                 "payload": data['term'].__str__()})

    log.info(q.query.__str__())
    log.info(ser.context.__str__())

    return ser.context


def read_input():
    """This method reads the input file which is in gzip format"""
    tbmms = ParliamentText.objects.filter(document_type='catalog')

    for i, line in enumerate(tbmms):
        if (i % 1000 == 0):
            print("read " + i.__str__() + " reviews")

        # do some pre-processing and return a list of words for each review text
        yield gensim.utils.simple_preprocess(line.text)


def mostSimilar(word, model):
    try:
        print('trying here', word, model.__str__())
        similar = model.wv.most_similar(positive=word)
        print('similar=gensim.model.wv.most_similar(positive=word)\n')
        count = str(model.wv.vocab[word].count)
        print('count=str(gensim.model.wv.vocab[word].count)\n')

        result = []
        print('result=[]\n')

        result.append(similar)
        print('result.append(similar)\n')

        result.append(count)
        print('result.append(count)\n')

        return (result)

    except:
        print('EXCEPTION HERE')


def W2V():
    documents = list(read_input())
    print('documents = list(read_input())')

    # if model cache is not exist , it generate
    # model = gensim.models.Word2Vec(documents, size=150, window=5, min_count=2, workers=4)
    #
    # model.save("tbmmW2v.model")

    model = gensim.models.Word2Vec.load("tbmmW2v.model")
    print(' model = gensim.models.Word2Vec.load("tbmmW2v.model")')

    model.train(documents, total_examples=len(documents), epochs=10)
    print('model.train(documents, total_examples=len(documents), epochs=10)')

    return mostSimilar("savaş", model)


def simpleW2V(query):
    txt_search_input = query['txt_search_input']

    if txt_search_input is not None:
        start_time = time.time()

        print(txt_search_input)

        documents = list(read_input())
        print('documents = list(read_input())')

        # if model cache is not exist , it generate
        # model = gensim.models.Word2Vec(documents, size=150, window=5, min_count=2, workers=4)
        #
        # model.save("tbmmW2v.model")

        model = gensim.models.Word2Vec.load("tbmmW2v.model")
        print(' model = gensim.models.Word2Vec.load("tbmmW2v.model")')

        model.train(documents, total_examples=len(documents), epochs=10)
        print('model.train(documents, total_examples=len(documents), epochs=10)')
        result = mostSimilar(txt_search_input.__str__(), model)
        print("---Finished !!!  %s seconds ---" % (time.time() - start_time))
        duration = time.time() - start_time

        ser = SimpleSerializer(
            context={"type": "advancedw2v", "query_string": txt_search_input.__str__(),"duration": duration.__str__(),
                     "payload": result.__str__()})
        log.info(ser.context.__str__())
        return ser.context


def advancedW2V(query):
    txt_advanced_search_input = query['txt_advanced_search_input']
    return txt_advanced_search_input
# path = get_tmpfile("tbmmW2v.model")
# model = gensim.models.Word2Vec(documents, size=150, window=5, min_count=2, workers=4)
# model.save("tbmmW2v.model")
# model = gensim.models.Word2Vec.load("tbmmW2v.model")
# model.train(documents, total_examples=len(documents), epochs=10)
