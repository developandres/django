# Generated by Django 4.2.5 on 2023-09-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senaback', '0004_alter_usuarios_nombre_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='nombre_2',
            field=models.CharField(max_length=12),
        ),
    ]
