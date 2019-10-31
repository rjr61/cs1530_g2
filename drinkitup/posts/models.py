import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_author = models.CharField(max_length=64)
    post_drink = models.CharField(max_length=64, null=True)
    post_text = models.CharField(max_length=200)
    post_location = models.CharField(max_length=64, null=True)
    post_score = models.IntegerField(default=0)
    post_url = models.CharField(max_length=64, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=64)
    comment_text = models.CharField(max_length=200)
    comment_score = models.IntegerField(default=0)
    comment_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
