from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Reaction(models.Model):
    """
    Reaction model, related to a User instance (owner)
    and Post. The 'unique_together' attribute ensures
    that Users can only choose one reaction type per post.
    """
    reaction_choices = [
        ('CROWN', 'CROWN'),
        ('GOOD', 'GOOD'),
        ('LOVE', 'LOVE'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='reactions'
    )
    reaction = models.CharField(max_length=50, choices=reaction_choices)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
