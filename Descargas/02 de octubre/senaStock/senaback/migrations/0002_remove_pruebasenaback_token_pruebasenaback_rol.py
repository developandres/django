# Generated by Django 4.2.4 on 2023-09-07 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senaback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pruebasenaback',
            name='token',
        ),
        migrations.AddField(
            model_name='pruebasenaback',
            name='rol',
            field=models.CharField(default='rol', max_length=15),
        ),
    ]
