# Generated by Django 4.2.7 on 2024-04-02 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessert',
            old_name='image',
            new_name='dessert_image',
        ),
    ]
