# Generated by Django 2.2.6 on 2019-10-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_score',
            field=models.IntegerField(default=0),
        ),
    ]
