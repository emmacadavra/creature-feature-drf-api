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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        ralof = User.objects.create_user(username='ralof', password='pass')
        meridia = User.objects.create_user(username='meridia', password='pass')
        Post.objects.create(
            owner=ralof, title='hey, you...',
            content='...youre finally awake'
        )
        Post.objects.create(
            owner=meridia, title='surprise',
            content='A NEW HAND TOUCHES THE BEACON'
        )

    def test_can_retrieve_post_with_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'hey, you...')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_with_invalid_id(self):
        response = self.client.get('/posts/777/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_posts(self):
        self.client.login(username='ralof', password='pass')
        response = self.client.put(
            '/posts/1/',
            {'title': 'you were trying to cross the border, right?'}
        )
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(
            post.title, 'you were trying to cross the border, right?'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_user_posts(self):
        self.client.login(username='meridia', password='pass')
        response = self.client.put(
            '/posts/1/', {'title': 'A NEW HAND TOUCHES THE BEACON'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
