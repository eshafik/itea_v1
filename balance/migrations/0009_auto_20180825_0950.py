# Generated by Django 2.0.5 on 2018-08-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0008_auto_20180824_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualbalance',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='organizationbalance',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
