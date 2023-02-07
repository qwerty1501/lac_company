from django.shortcuts import render
from rest_framework import generics

from .serializers import FeedbackLinkSerializers
from .models import FeedbackLink


class FeedbackLinkCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackLinkSerializers
    queryset = FeedbackLink.objects.all()
    
    
class FeedbackLinkDeleteView(generics.DestroyAPIView):
    serializer_class = FeedbackLinkSerializers()
    queryset = FeedbackLink.objects.all()