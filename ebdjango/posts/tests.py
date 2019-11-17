from django.test import TestCase

import datetime

from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse

from .models import Post

class PostModelTests(TestCase):
    def test_was_published_recently_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date = time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_post = Post(pub_date = time)
        self.assertIs(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Post(pub_date = time)
        self.assertIs(recent_post.was_published_recently(), True)

class LoginTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')

    def test_correct_user_correct_password_successful(self):
        self.client.login(username='username', password='password')
        response=self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)

    def test_incorrect_user_correct_password_successful(self):
        self.client.login(username='notusername', password='password')
        response=self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 302)

    def test_correct_user_incorrect_password_successful(self):
        self.client.login(username='username', password='notpassword')
        response=self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 302)

    def test_incorrect_user_incorrect_password_successful(self):
        self.client.login(username='notusername', password='notpassword')
        response=self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 302)