# Generated by Django 4.2.6 on 2023-11-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_buildingconsumptionenergy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingconsumption',
            name='house_consumption',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]