# Generated by Django 4.2.5 on 2023-10-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_remove_band_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
