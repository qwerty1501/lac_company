from django.urls import path
from .views import NewsListAPIView, NewsRetrieveAPIView


urlpatterns = [
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view())
]