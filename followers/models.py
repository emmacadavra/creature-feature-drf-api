from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model which handles the following of users. The 'related_name'
    attribute is given to 'owner' and 'followed' so that Django can
    differentiate between them, as they are both User model instances:
    'owner' is a User that is following another User, and 'followed' is the
    User being followed by 'owner'. The 'unique_together' attribute ensures
    users can't follow the same user more than once.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
