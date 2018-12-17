from django.shortcuts import render

from research.query import simpleQuery
# Create your views here.
from django.http import HttpResponse

from webapp.corpus.models import ParliamentText


def index(request):
    context=None
    if request.method == 'POST':


        # SIMPLE
        if request.POST['txt_search_input']:
           response= simpleQuery(query=request.POST)
            # data = request.POST['txt_search_input']



        #     ADVANCED
        # if request.POST['txt_advanced_search_input']:
        #     query = request.POST['txt_advanced_search_input']



        # query='Reis'
        # birlesim = ParliamentText.objects.filter(text__icontains='amerika')
        # data = {}
        # data['term'] = []
        # for i in range(1, 5):
        #     data['term'].append(birlesim.filter(term=(i)).count())
        # one = data['term']

        context = {'query': response}

    return render(request, 'research/index.html', context)

# {"type":"simple},"payload":{asdasn}}
