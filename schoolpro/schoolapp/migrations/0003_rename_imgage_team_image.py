# Generated by Django 4.1.5 on 2023-01-31 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='imgage',
            new_name='image',
        ),
    ]