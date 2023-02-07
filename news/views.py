from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News
from .serializers import NewsSerializers


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    
    
class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers