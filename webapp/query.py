from webapp.corpus.models import ParliamentText

birlesim=ParliamentText.objects.filter(text__icontains='amerika')

# data={}
# data['donemler']=[]
# for i in range(1,25):
#     data['donemler'].append(birlesim.filter(term=i).count())
# print(data['donemler'])


