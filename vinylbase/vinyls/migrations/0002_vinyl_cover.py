# Generated by Django 3.0.3 on 2021-11-26 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinyls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinyl',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]