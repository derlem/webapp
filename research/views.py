from django.shortcuts import render

from research.query import simpleQuery, advancedQuery


def index(request):
    context = None
    if request.method == 'POST':

        # SIMPLE
        if request.POST['txt_search_input']:
            response = simpleQuery(query=request.POST)

        # ADVANCED
        elif request.POST['txt_advanced_search_input']:
            response = advancedQuery(query=request.POST)

        else:
            response = None

        context = {'query': response}

    return render(request, 'research/index.html', context)
