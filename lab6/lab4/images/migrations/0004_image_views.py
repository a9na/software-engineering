# Generated by Django 5.1.3 on 2024-11-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_image_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
