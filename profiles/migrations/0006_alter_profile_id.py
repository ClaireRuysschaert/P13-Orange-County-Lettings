# Generated by Django 4.2.16 on 2024-09-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0005_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]