# Generated by Django 3.0 on 2024-07-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0003_transfer_profile_data'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Profile",
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="Profile",
                    table="profile_profile",
                ),
            ],
        ),
    ]
