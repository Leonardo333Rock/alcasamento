# Generated by Django 5.0.6 on 2024-09-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_presentes_ganho'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentes_ganho',
            name='id_presente',
            field=models.IntegerField(default=0),
        ),
    ]
