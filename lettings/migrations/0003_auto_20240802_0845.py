# Generated by Django 3.0 on 2024-08-02 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20240801_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letting',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
    ]
