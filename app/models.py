from django.db import models

class EnergyConsumption(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    total_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    attic_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    basement_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    heating_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    water_m3 = models.DecimalField(max_digits=10, decimal_places=2)
    total_heat_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    water_heat_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    house_heat_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    photovoltaic = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.year} - {self.month}"
