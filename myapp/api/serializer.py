from rest_framework import serializers
from ..models import MyModel


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('id', 'name', 'age', 'profesion', 'created_at')
        read_only_fields = ('created_at',)
