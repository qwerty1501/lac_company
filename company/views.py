from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import CreateStaff, Services, Partners, Reviews
from .serializers import CreateStaffSerializers, ServicesSerializers, PartnersSerializers, ReviewsSerializers

# Создание специалистов
class CreateStaffListAPIView(ListAPIView):
    queryset = CreateStaff.objects.all()
    serializer_class = CreateStaffSerializers
    
    
class CreateStaffRetrieveAPIView(RetrieveAPIView):
    queryset = CreateStaff.objects.all()
    serializer_class = CreateStaffSerializers
    
# Создание услуг
class ServicesListAPIView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers

    
class ServicesRetrieveAPIView(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    
    
# Создание партнёра
class PartnersListAPIView(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializers

    
class PartnersRetrieveAPIView(RetrieveAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializers
    
# Создание отзывов
class ReviewsListAPIView(ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    
    
class ReviewsRetrieveAPIView(RetrieveAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers