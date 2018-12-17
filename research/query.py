from research.serializers import *
import logging

from webapp.corpus.models import ParliamentText

log = logging.getLogger(__name__)

def simpleQuery(query):
    print("query:-> ", query)
    if query['txt_search_input']:
        txt_search_input = query['txt_search_input']
        q = ParliamentText.objects.filter(text__icontains=txt_search_input)
        q.filter(document_type='session')
        data = {}
        data['term'] = []
        for i in range(1, 2):
            data['term'].append(q.filter(term=(i)).count())

        ser = SimpleSerializer(
            context={"type": "simple", "query_string": txt_search_input.__str__(), "payload": data['term'].__str__()})

        log.info(ser.context.__str__())
        return ser.context
