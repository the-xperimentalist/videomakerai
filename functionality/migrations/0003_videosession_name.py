# Generated by Django 3.1 on 2020-08-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0002_auto_20200815_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosession',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
