from research.serializers import *


def simpleQuery(query):
    print("query:-> ", query)
    if query['txt_search_input']:
        txt_search_input = query['txt_search_input']
        q = ParliamentText.objects.filter(text__icontains=txt_search_input)
        q.filter(document_type='session')
        data = {}
        data['term'] = []
        for i in range(1, 5):
            data['term'].append(q.filter(term=(i)).count())

        ser = SimpleSerializer(
            context={"type": "simple", "query_string": txt_search_input, "payload": data['term']})

        return ser
