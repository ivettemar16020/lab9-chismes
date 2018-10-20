from rest_framework import serializers
from .models import Chisme


class ChismeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'date',
        )
        model = Chisme