from django.urls import path

from . import views

app_name = "research"

urlpatterns = [
    path('', views.index, name='index'),
    path('query', views.query_view, name='query_view'),
    path('query/advanced', views.advanced_query_view, name='advanced_query_view'),
    path('word2vec/advanced', views.advanced_word2vec_view, name='advanced_word2vec_view'),
    path('word2vec', views.word2vec_view, name='word2vec_view')
]
