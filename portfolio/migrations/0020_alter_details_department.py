# Generated by Django 5.0.6 on 2024-05-25 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_alter_details_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.department'),
        ),
    ]
