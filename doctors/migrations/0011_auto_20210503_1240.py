# Generated by Django 3.1.5 on 2021-05-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0010_doctor_hospitalregisterationnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='ProfilePhoto',
            field=models.FileField(default='static/images/boy_avatar.jpg', upload_to='DoctorPhotos/'),
        ),
    ]
