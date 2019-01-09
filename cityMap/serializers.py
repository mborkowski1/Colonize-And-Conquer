from rest_framework import serializers
from .models import CityOwned, Housing, Farms, PowerPlant, Mines, Roads, TownHall, Barracks
from .models import Infantry, HInfantry, LTanks, HTanks, Motorized, Planes


class CityOwnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityOwned
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = '__all__'


class FarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = '__all__'


class PowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlant
        fields = '__all__'


class MinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mines
        fields = '__all__'


class RoadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roads
        fields = '__all__'


class TownHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TownHall
        fields = '__all__'


class BarracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barracks
        fields = '__all__'


class InfantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Infantry
        fields = '__all__'


class HInfantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HInfantry
        fields = '__all__'


class LTanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LTanks
        fields = '__all__'


class HTanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTanks
        fields = '__all__'


class MotorizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorized
        fields = '__all__'


class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = '__all__'
























