from answers.models import Message
from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket


class MessageSerializer(serializers.ModelSerializer):
    User = get_user_model()

#Display User's username instead of id
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all())

#Display title of related ticket instead of id
    to_ticket = serializers.SlugRelatedField(slug_field='title',
                                             queryset=Ticket.objects.all())

    class Meta:

        fields = ('id', 'to_ticket', 'author', 'body', 'created', )
        model = Message
