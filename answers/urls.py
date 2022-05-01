from answers.views import MessageList
from django.urls import path

urlpatterns = [
    path('messages/', MessageList.as_view()),
]
