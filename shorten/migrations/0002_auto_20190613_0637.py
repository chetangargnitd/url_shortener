# Generated by Django 2.1 on 2019-06-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
    ]
