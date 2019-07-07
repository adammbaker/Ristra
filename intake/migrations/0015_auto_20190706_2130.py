# Generated by Django 2.2.3 on 2019-07-07 03:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0014_auto_20190706_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='country_of_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='intake.CountryOfOrigin'),
        ),
        migrations.AlterField(
            model_name='intakebus',
            name='arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 3, 30, 6, 608590, tzinfo=utc), verbose_name='Arrival time of bus'),
        ),
    ]
