# Generated by Django 5.0.6 on 2024-05-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]