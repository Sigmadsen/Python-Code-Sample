# Generated by Django 2.1.4 on 2019-02-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20190209_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tolerance',
            field=models.FloatField(default=0.4, verbose_name='Tolerance'),
        ),
    ]