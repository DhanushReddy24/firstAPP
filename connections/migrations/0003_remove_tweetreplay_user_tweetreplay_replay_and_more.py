# Generated by Django 4.2 on 2023-05-11 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0002_rename_tweets_tweet_tweetreplay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetreplay',
            name='user',
        ),
        migrations.AddField(
            model_name='tweetreplay',
            name='replay',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tweetreplay',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connections.tweet'),
        ),
    ]