# Generated by Django 3.2.9 on 2021-11-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20211104_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
