# Generated by Django 5.0.6 on 2024-05-22 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_questions_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='count',
        ),
    ]
