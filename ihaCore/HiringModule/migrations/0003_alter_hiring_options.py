# Generated by Django 5.0.6 on 2024-05-09 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HiringModule', '0002_auto_20240508_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hiring',
            options={'permissions': [('user_list_hiring', 'Can list user hirings')]},
        ),
    ]
