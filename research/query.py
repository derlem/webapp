import gensim
from django.db.models import Case, When
# from gensim.test.utils import common_texts, get_tmpfile

from research.serializers import *
import logging

from webapp.corpus.models import ParliamentText

log = logging.getLogger(__name__)


def simpleQuery(query):
    txt_search_input = query['txt_search_input']
    q = ParliamentText.objects.filter(text__icontains=txt_search_input)
    q.filter(document_type='session')
    data = {}
    data['term'] = []
    for i in range(1, 26):
        data['term'].append(q.filter(term=(i)).count())

    ser = SimpleSerializer(
        context={"type": "simple", "query_string": txt_search_input.__str__(), "payload": data['term'].__str__()})
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

    ser = SimpleSerializer(
        context={"type": "advanced", "query_string": txt_advanced_search_input.__str__(),
                 "payload": data['term'].__str__()})
    log.info(q.query.__str__())
    log.info(ser.context.__str__())
    return ser.context

#
# def read_input():
#     """This method reads the input file which is in gzip format"""
#     tbmms = ParliamentText.objects.all()
#
#     # logging.info("reading TBMM ...this may take a while")
#
#     for i, line in enumerate(tbmms):
#         # if (i % 1000 == 0):
#         # logging.info("read {0} reviews".format(i))
#
#         # do some pre-processing and return a list of words for each review text
#         yield gensim.utils.simple_preprocess(line.text)
#
#
# def mostSimilar(word):
#     try:
#         similar=gensim.model.wv.most_similar(positive=word)
#         count=str(gensim.model.wv.vocab[word].count)
#         result=[]
#         result.append(similar)
#         result.append(count)
#         return (result)
#
#     except:
#         print('EXCEPTION')
#

def simpleW2V(query):
    txt_search_input = query['txt_search_input']
    return txt_search_input

    # documents = list(read_input())
    #
    # # if model cache is not exist , it generate
    # model = gensim.models.Word2Vec(documents, size=150, window=5, min_count=2, workers=4)
    # model.save("tbmmW2v.model")
    #
    # model = gensim.models.Word2Vec.load("tbmmW2v.model")
    # model.train(documents, total_examples=len(documents), epochs=10)
    # return mostSimilar(txt_search_input)


def advancedW2V(query):
    txt_advanced_search_input = query['txt_advanced_search_input']
    return txt_advanced_search_input
# path = get_tmpfile("tbmmW2v.model")
# model = gensim.models.Word2Vec(documents, size=150, window=5, min_count=2, workers=4)
# model.save("tbmmW2v.model")
# model = gensim.models.Word2Vec.load("tbmmW2v.model")
# model.train(documents, total_examples=len(documents), epochs=10)
