# Generated by Django 4.0.5 on 2022-06-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.BigIntegerField(default=0),
        ),
    ]
