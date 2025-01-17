# Generated by Django 2.2.24 on 2022-09-20 06:52

from django.db import migrations

from django.db import migrations

def new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)

class Migration(migrations.Migration):
    dependencies = [
        ('property', '0002_auto_20220919_0903'),
    ]

    operations = [
        migrations.RunPython(new_building),
    ]
