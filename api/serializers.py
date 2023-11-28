from rest_framework import serializers
from .models import NewsModels


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsModels
        fields = '__all__'


