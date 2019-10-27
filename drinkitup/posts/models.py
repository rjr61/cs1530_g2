import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_author = models.CharField(max_length=64)
    post_text = models.CharField(max_length=200)
    post_score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)