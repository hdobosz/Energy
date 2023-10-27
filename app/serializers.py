from rest_framework import serializers
from .models import EnergyConsumption

class EnergySerializer(serializers.ModelSerializer):
    class Meta:

        model = EnergyConsumption

        fields = '__all__'