# Generated by Django 4.2 on 2023-05-11 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connections', '0003_remove_tweetreplay_user_tweetreplay_replay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetreplay',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
