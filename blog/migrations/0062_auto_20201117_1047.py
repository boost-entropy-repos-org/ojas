# Generated by Django 3.0.5 on 2020-11-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0061_auto_20201117_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=500, unique_for_date='name'),
        ),
    ]