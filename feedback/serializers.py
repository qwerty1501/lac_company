from rest_framework import serializers
from .models import FeedbackLink


class FeedbackLinkSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedbackLink
        fields = '__all__'