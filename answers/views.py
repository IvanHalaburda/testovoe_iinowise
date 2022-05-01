from answers.serializers import MessageSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from tickets.models import Ticket


class MessageList(generics.ListCreateAPIView):
#Quryset consists of messages, related to ticket with specific id 
    def get_queryset(self):
        related_ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        queryset = related_ticket.messages.all()
        return queryset
    serializer_class = MessageSerializer
