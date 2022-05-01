import pytest
from answers.models import Message
from django.contrib.auth.models import User
from tickets.models import Ticket


def test_create_ticket(db):
    testuser = User.objects.create_user(username='testuser', password='askjdfjkad')
    testuser.save()
    testticket = Ticket.objects.create(status='Active', title='problem',
                                       author = testuser,body = 'problems' )
    testticket.save()

    testanswer = Message.objects.create(to_ticket = testticket, author = testuser,
                                        body= 'answer')
    testanswer.save()
    
    assert testuser.username == 'testuser'
    assert testanswer.body == 'answer'
    assert testanswer.to_ticket.title == 'problem'
