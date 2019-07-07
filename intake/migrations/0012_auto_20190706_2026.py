# Generated by Django 2.2.3 on 2019-07-07 02:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0011_auto_20190706_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='locations',
            field=models.ManyToManyField(to='intake.Location', verbose_name='Locations'),
        ),
        migrations.AlterField(
            model_name='intakebus',
            name='arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 2, 26, 49, 974791, tzinfo=utc), verbose_name='Arrival time of bus'),
        ),
    ]
