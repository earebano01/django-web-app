# Generated by Django 4.2.5 on 2023-09-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='albums',
            field=models.TextField(default='null'),
        ),
    ]
