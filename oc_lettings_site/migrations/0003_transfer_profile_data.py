# Generated by Django 3.0 on 2024-07-26 14:38

from django.db import migrations, transaction

def transfer_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    UserModel = apps.get_model("auth", "User")
    
    
    try:
        with transaction.atomic():
            NewProfile.objects.bulk_create(
                NewProfile(
                    user=UserModel.objects.get(id=old_object.user.id),
                    favorite_city=old_object.favorite_city,
                )
                for old_object in OldProfile.objects.all()
            )
    except Exception as e:
        print(f"Error occurred during data transfer: {e}")
        raise


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20240726_1402'),
    ]

    operations = [
        migrations.RunPython(transfer_data,  migrations.RunPython.noop),
    ]