# Generated by Django 5.0.1 on 2024-04-02 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='file',
            new_name='image',
        ),
    ]
