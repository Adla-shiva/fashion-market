# Generated by Django 4.2.5 on 2023-10-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
