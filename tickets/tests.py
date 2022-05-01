import pytest
from django.contrib.auth.models import User
from tickets.models import Ticket


def test_create_ticket(db):
    testuser = User.objects.create_user(username='testuser', password='askjdfjkad')
    testuser.save()
    testticket = Ticket.objects.create(status='Active', title='problem',
                                       author = testuser,body = 'problems' )
    testticket.save()

    assert testuser.username == 'testuser'
    assert testticket.title == "problem"
    assert testticket.body == "problems"
    assert testticket.status == "Active"
