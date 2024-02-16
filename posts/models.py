from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # ADD DOCSTRING

    class PostObjects(models.Manager):
        # ADD DOCSTRING
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    category_choices = [
        ('fluffy', 'Facinorous Fluffballs'),
        ('scaly', 'Reptillian Villains'),
        ('feathers', 'Feathered Fiends'),
    ]
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II'),
    ]
    post_options = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_kkmzvb', blank=True
    )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal'
    )
    category = models.CharField(
        max_length=40,
        choices=category_choices,
        default='fluffy'
    )
    status = models.CharField(
        max_length=10,
        choices=post_options,
        default='published'
    )
    objects = models.Manager()
    post_objects = PostObjects()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
