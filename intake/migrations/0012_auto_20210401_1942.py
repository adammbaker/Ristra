# Generated by Django 3.1.7 on 2021-04-02 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0011_auto_20210330_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asylee',
            name='medicals',
        ),
        migrations.DeleteModel(
            name='Medical',
        ),
    ]
