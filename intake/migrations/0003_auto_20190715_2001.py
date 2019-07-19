# Generated by Django 2.2.3 on 2019-07-16 02:01

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0002_campaign_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
    ]