# Generated by Django 3.2.12 on 2022-07-01 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='preview',
            new_name='image',
        ),
    ]
