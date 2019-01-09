from rest_framework import viewsets
from .models import CityOwned, Housing, Farms, PowerPlant, Mines, Roads, TownHall, Barracks
from .models import Infantry, HInfantry, LTanks, HTanks, Motorized, Planes
from .serializers import CityOwnedSerializer, HousingSerializer, FarmsSerializer, PowerPlantSerializer, MinesSerializer, HInfantrySerializer, InfantrySerializer
from .serializers import LTanksSerializer, HTanksSerializer, MotorizedSerializer, PlanesSerializer, BarracksSerializer, TownHallSerializer, RoadsSerializer


class CityOwnedViewSet(viewsets.ModelViewSet):
    queryset = CityOwned.objects.all()
    serializer_class = CityOwnedSerializer


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer


class FarmsViewSet(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer


class PowerPlantViewSet(viewsets.ModelViewSet):
    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer


class MinesViewSet(viewsets.ModelViewSet):
    queryset = Mines.objects.all()
    serializer_class = MinesSerializer


class HInfantryViewSet(viewsets.ModelViewSet):
    queryset = HInfantry.objects.all()
    serializer_class = HInfantrySerializer


class InfantryViewSet(viewsets.ModelViewSet):
    queryset = Infantry.objects.all()
    serializer_class = InfantrySerializer


class LTanksViewSet(viewsets.ModelViewSet):
    queryset = LTanks.objects.all()
    serializer_class = LTanksSerializer


class HTanksViewSet(viewsets.ModelViewSet):
    queryset = HTanks.objects.all()
    serializer_class = HTanksSerializer


class MotorizedViewSet(viewsets.ModelViewSet):
    queryset = Motorized.objects.all()
    serializer_class = MotorizedSerializer


class PlanesViewSet(viewsets.ModelViewSet):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer


class BarracksViewSet(viewsets.ModelViewSet):
    queryset = Barracks.objects.all()
    serializer_class = BarracksSerializer


class TownHallViewSet(viewsets.ModelViewSet):
    queryset = TownHall.objects.all()
    serializer_class = TownHallSerializer


class RoadsViewSet(viewsets.ModelViewSet):
    queryset = Roads.objects.all()
    serializer_class = RoadsSerializer
















