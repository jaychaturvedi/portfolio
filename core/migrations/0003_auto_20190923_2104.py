# Generated by Django 2.2.3 on 2019-09-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190923_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentwork',
            name='image',
            field=models.ImageField(default='default.png', upload_to='works'),
        ),
    ]
