# Generated by Django 3.0.5 on 2020-11-13 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_auto_20201113_2103'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Viewer',
        ),
    ]