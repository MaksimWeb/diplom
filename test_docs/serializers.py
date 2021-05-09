from .models import TestDocs
from rest_framework import serializers
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

class SHistory(serializers.ModelSerializer):
    def __init__(self, model, *args, fields='__all__', **kwargs):
        self.Meta.model = model
        self.Meta.fields = fields
        super().__init__()

    class Meta:
        pass


class TestDocsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TestDocs

    history = serializers.SerializerMethodField()

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = '__all__'
        serializer = SHistory(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
        serializer.is_valid()
        return serializer.data


class AllHistory(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = HistoricalRecords
