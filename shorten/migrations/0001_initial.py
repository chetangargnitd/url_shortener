# Generated by Django 2.1 on 2019-06-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('shrinked_url', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('original_url', models.CharField(max_length=2083)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
