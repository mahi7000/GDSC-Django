# Generated by Django 5.0.2 on 2024-03-03 14:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField(max_length=1000)),
                ('category', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=list, size=None)),
            ],
        ),
    ]
