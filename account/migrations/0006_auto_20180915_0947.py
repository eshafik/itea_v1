# Generated by Django 2.0.5 on 2018-09-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_finance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='itea_status',
            field=models.CharField(choices=[('member', 'General Member'), ('executive', 'Executive Member'), ('public', 'Public')], default='public', max_length=20),
        ),
    ]
