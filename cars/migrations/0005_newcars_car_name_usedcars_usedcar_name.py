# Generated by Django 4.1.7 on 2023-04-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_newcars_options_newcars_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcars',
            name='car_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usedcars',
            name='usedcar_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
