import sys

from django.db import models
from tickets.models import Ticket

sys.path.append('..')


class Message(models.Model):
    to_ticket = models.ForeignKey(Ticket, related_name='messages',
                                  on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.body
