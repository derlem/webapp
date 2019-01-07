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
    if request.method == 'POST':

        if request.POST['txt_advanced_search_input']:
            response = advancedQuery(request.POST)
            # response = {'type': 'advanced compare', 'query_string': "['altin','gumus','']",
            #             'duration': '233.32243132591248',
            #             'payload': "{'txt_advanced_search_input': '[2461, 4324, 1929, 2267, 1753, 2484, 2093, 5362, 6427, 3700, 3098, 0, 0, 0, 0, 0, 7352, 11257, 14829, 11241, 15373, 27177, 20518, 10441, 0]', 'txtcompare1': '[1036, 2278, 836, 1644, 837, 1271, 742, 1540, 1955, 1947, 1205, 0, 0, 0, 0, 0, 1077, 1497, 2235, 1539, 1327, 2125, 1141, 1905, 0]'}"}
            durationTime = response['duration']

            if response['type'] == 'advanced compare':
                response
                print('payload\n\n\n\n\t')
                print(response['payload'])
                chart_data = []
                qsArr = eval(response['query_string'])
                header = []
                header.append('Term')
                for querstr in qsArr:
                    if querstr[0] is not 'empty':
                        header.append(querstr[0])
                chart_data.append(header)
                print('chart_data', chart_data)

                dic = eval(response["payload"])
                # print('dic', dic)

                # print(type(arr))
                for i in range(1, 26):
                    dizi = []
                    dizi.append((i).__str__() + '. Dönem')

                    ar0 = eval(dic['txt_advanced_search_input'])
                    dizi.append(ar0[i - 1])
                    if 'txtcompare1' in dic:
                        ar = eval(dic['txtcompare1'])
                        # print(i)
                        # print(ar, 'arrrr', type(ar))
                        dizi.append(ar[i - 1])
                    if 'txtcompare2' in dic:
                        ar2 = eval(dic['txtcompare2'])
                        dizi.append(ar2[i - 1])

                    chart_data.append(dizi)
                print('chardata', chart_data)
                context = {'query': response, 'chart_data': chart_data, 'durationTime': durationTime, 'isCompare': True}

            else:
                context = {'query': response}

    return render(request, 'research/advanced_query.html', context)
