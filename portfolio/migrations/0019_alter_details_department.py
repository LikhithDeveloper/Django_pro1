# Generated by Django 5.0.6 on 2024-05-25 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_details_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='portfolio.department'),
        ),
    ]
