# Generated by Django 4.2.7 on 2023-12-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitall', '0005_appointment_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='clinics/'),
        ),
    ]
