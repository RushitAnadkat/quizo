# Generated by Django 3.2.5 on 2021-07-18 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_quiz_is_given'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='is_given',
        ),
    ]
