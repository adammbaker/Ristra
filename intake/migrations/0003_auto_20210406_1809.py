# Generated by Django 3.1.7 on 2021-04-07 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0002_auto_20210405_2216'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalAge',
        ),
        migrations.RenameField(
            model_name='historicalorganization',
            old_name='historical_days_at_border',
            new_name='historical_days_traveling',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='historical_days_at_border',
            new_name='historical_days_traveling',
        ),
        migrations.DeleteModel(
            name='HistoricalData',
        ),
    ]
