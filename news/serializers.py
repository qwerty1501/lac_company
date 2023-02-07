from rest_framework import serializers as s
from .models import News


class NewsSerializers(s.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'