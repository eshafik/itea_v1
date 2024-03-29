# Generated by Django 2.0.5 on 2018-08-23 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('student', 'Student'), ('employed', 'Employed'), ('unemployed', 'Unemployed')], default='student', max_length=10)),
                ('status_details', models.TextField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('current_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
