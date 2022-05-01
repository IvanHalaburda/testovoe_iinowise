from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    User = get_user_model()
  #Display User's username instead of bare id
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all())

    class Meta:
        fields = ('id', 'status', 'title', 'author',
                  'body', 'created', 'updated', )
        model = Ticket
