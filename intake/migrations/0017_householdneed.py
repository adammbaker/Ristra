# Generated by Django 3.1.7 on 2021-04-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0016_headofhousehold_detention_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need', models.CharField(max_length=100, verbose_name='Household Need')),
            ],
        ),
    ]
