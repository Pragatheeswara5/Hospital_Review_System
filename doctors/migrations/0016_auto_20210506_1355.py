# Generated by Django 3.1.5 on 2021-05-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0015_auto_20210506_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='ProfilePhoto',
            field=models.FileField(default='DefaultPhotos/boy_avatar.jpg', upload_to='DoctorPhotos/'),
        ),
    ]
