# Generated by Django 2.0.5 on 2018-05-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0004_auto_20180507_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictmodel',
            name='Discharge',
            field=models.FloatField(),
        ),
    ]
