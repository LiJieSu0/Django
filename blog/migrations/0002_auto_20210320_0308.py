# Generated by Django 3.1.7 on 2021-03-20 07:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_name',
            new_name='article_title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='create_date',
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 7, 8, 28, 639401, tzinfo=utc), verbose_name='date published'),
        ),
    ]
