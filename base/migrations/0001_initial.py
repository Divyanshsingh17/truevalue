# Generated by Django 4.1.7 on 2023-04-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_img', models.ImageField(upload_to='agents/')),
                ('agent_name', models.CharField(max_length=100)),
                ('agent_desc', models.TextField()),
                ('agent_email', models.EmailField(max_length=50)),
                ('agent_phn_no', models.CharField(max_length=12)),
            ],
        ),
    ]
