# Generated by Django 4.2.6 on 2023-10-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('total_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('attic_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('basement_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('heating_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('water_m3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_heat_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('water_heat_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('house_heat_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photovoltaic', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
