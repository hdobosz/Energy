from django.db import models

class EnergyConsumption(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    total_kwh = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
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

class BuildingConsumption(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    total_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    water_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #house_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    ground_floor_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    attic_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    basement_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    heating_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Total Consumption: {self.total_consumption}\nWater Consumption: {self.water_consumption}\nHouse Consumption: {self.house_consumption}\nGround Floor Consumption: {self.ground_floor_consumption}\nAttic Consumption: {self.attic_consumption}\nBasement Consumption: {self.basement_consumption}\nHeating Consumption: {self.heating_consumption}"
    
