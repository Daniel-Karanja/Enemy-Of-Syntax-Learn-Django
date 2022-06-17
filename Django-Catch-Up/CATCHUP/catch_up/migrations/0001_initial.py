# Generated by Django 4.0.5 on 2022-06-16 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Puppy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catch_up.owner')),
            ],
        ),
    ]
