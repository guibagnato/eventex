# Generated by Django 2.2.1 on 2019-08-17 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
