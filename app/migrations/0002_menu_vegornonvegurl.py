# Generated by Django 5.0.1 on 2024-04-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='vegORnonvegurl',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
