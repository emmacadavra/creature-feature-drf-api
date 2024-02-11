from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='emma', password='pass')

    def test_can_list_posts(self):
        emma = User.objects.get(username='emma')
        Post.objects.create(owner=emma, title='abracadabra')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='emma', password='pass')
        response = self.client.post('/posts/', {'title': 'praise the sun!'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'prithee be careful'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
