# Generated by Django 2.2 on 2019-04-25 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190424_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testschedule',
            options={'ordering': ['student_last', 'student_first']},
        ),
    ]