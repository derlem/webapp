from django.shortcuts import render

from research.query import simpleQuery, advancedQuery, simpleW2V, advancedW2V


def index(request):
    return render(request, 'research/index.html')



def word2vec_view(request):
    context = None

    if request.method == 'POST':

        # SIMPLE
        if request.POST['txt_search_input']:
            response = simpleW2V(query=request.POST)

        # ADVANCED
        elif request.POST['txt_advanced_search_input']:
            response = advancedW2V(query=request.POST)

        else:
            response = None


        context = {'query': response}

    return render(request, 'research/word2vec.html', context)






def query_view(request):
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

    return render(request, 'research/query.html', context)


