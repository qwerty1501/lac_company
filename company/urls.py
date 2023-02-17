from django.urls import path
from .views import CreateStaffListAPIView, CreateStaffRetrieveAPIView, ServicesListAPIView, ServicesRetrieveAPIView,\
                PartnersListAPIView, PartnersRetrieveAPIView, ReviewsListAPIView, ReviewsRetrieveAPIView


urlpatterns = [
    path('create-staff/', CreateStaffListAPIView.as_view()),
    path('create-staff/<int:pk>/', CreateStaffRetrieveAPIView.as_view()),
    path('services/', ServicesListAPIView.as_view()),
    path('services/<int:pk>', ServicesRetrieveAPIView.as_view()),
    path('partners/', PartnersListAPIView.as_view()),
    path('partners/<int:pk>', PartnersRetrieveAPIView.as_view()),
    path('reviews/', ReviewsListAPIView.as_view()),
    path('reviews/<int:pk>', ReviewsRetrieveAPIView.as_view()),
]