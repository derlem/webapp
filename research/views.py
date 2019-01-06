import json

from django.shortcuts import render

from research.query import simpleQuery, advancedQuery, simpleW2V, advancedW2V


def index(request):
    return render(request, 'research/index.html')


def word2vec_view(request):
    context = None
    if request.method == 'POST':

        # SIMPLE
        if request.POST['txt_search_input']:
            durationTime = ''
            response = simpleW2V(query=request.POST)
            responsePayload = eval(response['payload'])
            durationTime = response['duration']
            if responsePayload is not None:
                chart_data = []
                chart_data.append(['Most Similar Words', request.POST['txt_search_input']])

                for index, value in enumerate(responsePayload[0]):
                    dizi = []
                    dizi.append(value[0])
                    dizi.append(value[1])
                    chart_data.append(dizi)

                context = {'query': response, 'chart_data': chart_data, 'durationTime': durationTime}

    return render(request, 'research/word2vec.html', context)


def advanced_word2vec_view(request):
    context = None
    if request.method == 'POST':

        if request.POST['txt_advanced_search_input']:
            response = advancedW2V(query=request.POST)
            context = {'query': response}

    return render(request, 'research/advanced_word2vec.html', context)


def query_view(request):
    context = None
    # response={'type': 'simple', 'query_string': 'bankası','payload': '[3101, 3504, 2012, 2922, 2072, 1525, 1753, 2387, 3580, 1836, 2051, 345, 273, 311, 267, 343, 3379, 5358, 6442, 4152, 8905, 9866, 6157, 1981, 0]'}

    if request.method == 'POST':

        # SIMPLE
        if request.POST['txt_search_input']:
            durationTime = ''
            response = simpleQuery(query=request.POST)
            durationTime = response['duration']
            chart_data = []
            chart_data.append(['Simple Query', response['query_string']])
            arr = eval(response["payload"])

            # print(type(arr))
            for index, number in enumerate(arr):
                dizi = []
                dizi.append((index + 1).__str__() + '. Dönem')
                dizi.append(number)
                chart_data.append(dizi)
            context = {'query': response, 'chart_data': chart_data, 'durationTime': durationTime}

    return render(request, 'research/query.html', context)


def advanced_query_view(request):
    context = None
    # response={'type': 'simple', 'query_string': 'bankası','payload': '[3101, 3504, 2012, 2922, 2072, 1525, 1753, 2387, 3580, 1836, 2051, 345, 273, 311, 267, 343, 3379, 5358, 6442, 4152, 8905, 9866, 6157, 1981, 0]'}
    if request.method == 'POST':
        if request.POST['txt_advanced_search_input']:
            response = advancedQuery(query=request.POST)
            context = {'query': response}

    return render(request, 'research/advanced_query.html', context)
