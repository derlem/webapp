from rest_framework import serializers
from webapp.corpus.models import ParliamentText

class SimpleSerializer(serializers.ModelSerializer):
    qtype = serializers.SerializerMethodField()
    payload = serializers.SerializerMethodField()
    class Meta:
        model=ParliamentText
        fields=[
            "qtype",
            "query_string",
            "payload"
        ]

    def get_qtype(self, obj):
        return self.context["type"].__str__()

    def get_payload(self, obj):
        return self.context["payload"]

    def get_query_string(self, obj):
        return self.context["query_string"].__str__()
