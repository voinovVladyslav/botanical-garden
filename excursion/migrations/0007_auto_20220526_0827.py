# Generated by Django 3.2.12 on 2022-05-26 05:27

from django.db import migrations, models
import excursion.models


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0006_auto_20220512_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='excursion_date',
            field=models.DateField(null=True, validators=[excursion.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='excursion',
            name='excursion_time',
            field=models.TimeField(null=True, validators=[excursion.models.validate_time]),
        ),
    ]
