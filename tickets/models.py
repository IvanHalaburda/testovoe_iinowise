from django.db import models


class Ticket(models.Model):
#Availabe statuses for ticket
    ACTIVE = 'Active'
    FROZEN = 'Frozen'
    SOLVED = 'Solved'
    STATUS = [
        (ACTIVE, 'Active'),
        (FROZEN, 'Frozen'),
        (SOLVED, 'Solved'),
    ]
    status = models.CharField(
        max_length=6,
        choices=STATUS,
        default=ACTIVE,
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
