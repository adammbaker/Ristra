# Generated by Django 2.2.3 on 2019-07-07 02:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0010_auto_20190706_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intakebus',
            name='arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 2, 16, 25, 97642, tzinfo=utc), verbose_name='Arrival time of bus'),
        ),
    ]
