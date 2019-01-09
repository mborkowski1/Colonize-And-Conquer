from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from mainPage.models import Server
# Create your models here.


class Barracks(models.Model):
    productionSpeed = models.IntegerField(default=1)
    pointsPerLvl = models.IntegerField(default=5)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class TownHall(models.Model):
    productionSpeed = models.IntegerField(default=1)
    lvlToUnlockPlanes = models.IntegerField(default=25)
    lvlToUnlockHtanks = models.IntegerField(default=20)
    lvlToUnlockLtanks = models.IntegerField(default=15)
    lvlToUnlockMotorized = models.IntegerField(default=10)
    lvlToUnlockHinfantry = models.IntegerField(default=5)
    pointsPerLvl = models.IntegerField(default=10)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Roads(models.Model):
    productionSpeed = models.IntegerField(default=1)
    pointsPerLvl = models.IntegerField(default=3)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Mines(models.Model):
    resourceProduction = models.IntegerField(default=10)
    pointsPerLvl = models.IntegerField(default=2)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class PowerPlant(models.Model):
    resourceProduction = models.IntegerField(default=10)
    pointsPerLvl = models.IntegerField(default=2)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Farms(models.Model):
    resourceProduction = models.IntegerField(default=10)
    pointsPerLvl = models.IntegerField(default=2)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Housing(models.Model):
    population = models.IntegerField(default=100)
    pointsPerLvl = models.IntegerField(default=1)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Infantry(models.Model):
    hp = models.IntegerField(default=10)
    attack = models.IntegerField(default=10)
    speed = models.IntegerField(default=20)
    capacity = models.IntegerField(default=30)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class HInfantry(models.Model):
    hp = models.IntegerField(default=30)
    attack = models.IntegerField(default=30)
    speed = models.IntegerField(default=10)
    capacity = models.IntegerField(default=10)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class LTanks(models.Model):
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=100)
    speed = models.IntegerField(default=80)
    capacity = models.IntegerField(default=100)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class HTanks(models.Model):
    hp = models.IntegerField(default=200)
    attack = models.IntegerField(default=100)
    speed = models.IntegerField(default=30)
    capacity = models.IntegerField(default=150)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Motorized(models.Model):
    hp = models.IntegerField(default=50)
    attack = models.IntegerField(default=50)
    speed = models.IntegerField(default=100)
    capacity = models.IntegerField(default=250)
    food = models.IntegerField(default=10)
    electrity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class Planes(models.Model):
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=200)
    speed = models.IntegerField(default=300)
    capacity = models.IntegerField(default=150)
    food = models.IntegerField(default=10)
    electricity = models.IntegerField(default=10)
    ore = models.IntegerField(default=10)


class CityOwned(models.Model):
    # techniczne
    city_owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100, default="City")
    is_capital = models.BooleanField(default=False)
    pos_x = models.IntegerField(default=1)
    pos_y = models.IntegerField(default=1)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, blank=True, null=True)

    # budynki
    town_hall = models.IntegerField(default=1)

    barracks = models.IntegerField(default=1)

    roads = models.IntegerField(default=1)

    mines = models.IntegerField(default=1)

    power_plant = models.IntegerField(default=1)

    farms = models.IntegerField(default=1)

    housing = models.IntegerField(default=1)

    # jendostki
    infantry = models.IntegerField(default=0)
    hinfantry = models.IntegerField(default=0)
    planes = models.IntegerField(default=0)
    ltanks = models.IntegerField(default=0)
    htanks = models.IntegerField(default=0)
    motorized = models.IntegerField(default=0)

    # zasoby
    food = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    ore = models.IntegerField(default=0)
    population = models.IntegerField(default=100)
    points = models.IntegerField(default=100)

    # technologie
    research_th1 = models.IntegerField(default=0)
    research_th2 = models.IntegerField(default=0)
    research_m = models.IntegerField(default=0)
    research_f = models.IntegerField(default=0)
    research_pp = models.IntegerField(default=0)
    research_r = models.IntegerField(default=0)
    research_h = models.IntegerField(default=0)
    research_b = models.IntegerField(default=0)

    def update_points(self, building):
        self.points += building.pointsPerLvl

    def __str__(self):
        return self.city_name
