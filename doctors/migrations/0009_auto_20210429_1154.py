# Generated by Django 3.1.5 on 2021-04-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_doctor_non_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Ratings_stars',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
    ]