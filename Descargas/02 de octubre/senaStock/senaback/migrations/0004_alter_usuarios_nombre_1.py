# Generated by Django 4.2.5 on 2023-09-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senaback', '0003_usuarios_remove_pruebasenaback_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='nombre_1',
            field=models.CharField(max_length=12),
        ),
    ]
