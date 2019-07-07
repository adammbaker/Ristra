# Generated by Django 2.2.3 on 2019-07-06 01:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0004_auto_20190705_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intakebus',
            name='arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 1, 34, 39, 447624, tzinfo=utc), verbose_name='Arrival time of bus'),
        ),
        migrations.AlterField(
            model_name='medical',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
