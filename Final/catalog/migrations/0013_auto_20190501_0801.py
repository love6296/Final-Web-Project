# Generated by Django 2.2 on 2019-05-01 13:01

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20190501_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='School phone number', max_length=31),
        ),
    ]
