# Generated by Django 2.1.4 on 2019-01-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0010_auto_20190125_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concretepersonactionhistory',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
