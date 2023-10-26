# Generated by Django 4.2.6 on 2023-10-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_buildingconsumption_attic_consumption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyconsumption',
            name='total_kwh',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]