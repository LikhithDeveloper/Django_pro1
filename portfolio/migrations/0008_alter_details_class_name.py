# Generated by Django 5.0.6 on 2024-05-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_delete_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='class_name',
            field=models.CharField(default='SOME STRING', max_length=10),
        ),
    ]
