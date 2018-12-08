from django.urls import path

from django.views.generic import TemplateView

app_name = "corpus"
urlpatterns = [
    path("", TemplateView.as_view(template_name="ngram_viewer/chart.html"), name="chart"),
]
