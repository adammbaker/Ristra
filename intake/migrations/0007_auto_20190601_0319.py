# Generated by Django 2.2.1 on 2019-06-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0006_auto_20190601_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Location name'),
        ),
    ]