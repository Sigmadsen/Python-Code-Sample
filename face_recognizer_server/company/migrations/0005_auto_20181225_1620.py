# Generated by Django 2.1.4 on 2018-12-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_door_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Start tracking'), (2, 'Stop tracking'), (3, 'Nothing')], default=3, verbose_name='Status'),
        ),
    ]
