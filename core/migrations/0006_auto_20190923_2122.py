# Generated by Django 2.2.3 on 2019-09-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(max_length=250, verbose_name='Devicon'),
        ),
    ]
