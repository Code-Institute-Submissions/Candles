# Generated by Django 3.0.5 on 2020-05-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
