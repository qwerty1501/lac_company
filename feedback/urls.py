from django.urls import path
from .views import FeedbackLinkCreateListView, FeedbackLinkDeleteView


urlpatterns = [
    path('feedback/', FeedbackLinkCreateListView.as_view()),
    path('feedback/delete/<int:pk>/', FeedbackLinkDeleteView.as_view()),
]