from django.urls import path

from . import views

app_name = "research"

urlpatterns = [
    path('', views.index, name='index'),
    path('query', views.query_view, name='query_view'),
    path('word2vec', views.word2vec_view, name='word2vec_view')
]
