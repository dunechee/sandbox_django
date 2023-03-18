# Generated by Django 4.1.2 on 2023-03-16 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bearID', models.IntegerField()),
                ('pTT_ID', models.IntegerField()),
                ('capture_lat', models.FloatField()),
                ('capture_long', models.FloatField()),
                ('sex', models.TextField()),
                ('age_class', models.TextField()),
                ('ear_applied', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
