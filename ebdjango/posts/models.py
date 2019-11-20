import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_author = models.CharField(max_length=64)
    post_drink = models.CharField(max_length=64, null=True)
    post_text = models.CharField(max_length=200)
    post_location = models.CharField(max_length=64, null=True)
    post_score = models.IntegerField(default=0)
    post_url = models.CharField(max_length=64, null=True, default="posts/cocktail.png")
    pub_date = models.DateTimeField('date published', default = timezone.now)
    
    WINE = 'WI'
    BEER = 'BR'
    COCKTAIL = 'CT'
    SHOT = 'SH'
    DRINK_CHOICES = (
        (WINE, 'wine'),
        ('BR', 'beer'),
        (COCKTAIL, 'cocktail'),
        (SHOT, 'shot'),
    )
    drink_type = models.CharField(max_length=2, choices=DRINK_CHOICES, default=COCKTAIL)

    def __str__(self):
        return self.post_drink

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=64)
    comment_text = models.CharField(max_length=200)
    comment_score = models.IntegerField(default=0)
    comment_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text


class Likers(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    like_author = models.CharField(max_length=64)
    val = models.BooleanField()
    def __str__(self):
        return self.like_author
