# Generated by Django 2.1.4 on 2019-01-31 16:24

from django.db import migrations, models
import face_recognizer_server.utils.upload_location


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0011_auto_20190130_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personvideo',
            name='uploaded_video_file',
            field=models.FileField(upload_to=face_recognizer_server.utils.upload_location.upload_video_of_person, verbose_name='Video'),
        ),
    ]
