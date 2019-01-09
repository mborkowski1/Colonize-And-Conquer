from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import cityMap.models
import alliance.models
# Create your models here.


class BattleRaport(models.Model):
    name = models.CharField(max_length=100, default="battle raport")
    have_seen = models.BooleanField(default=False)

    attacker = models.ForeignKey(User, related_name='attacker', on_delete=models.CASCADE)
    defender = models.ForeignKey(User, related_name='defender', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    cityA = models.ForeignKey(cityMap.models.CityOwned, related_name='attackvillage', on_delete=models.CASCADE)
    cityD = models.ForeignKey(cityMap.models.CityOwned, related_name='defensevillage', on_delete=models.CASCADE)

    stolen_food = models.IntegerField(default=0)
    stolen_energy = models.IntegerField(default=0)
    stolen_minerals = models.IntegerField(default=0)
    stolen_special_resource = models.IntegerField(default=0)

    infantryA = models.IntegerField(default=0)
    hinfantryA = models.IntegerField(default=0)
    planesA = models.IntegerField(default=0)
    ltanksA = models.IntegerField(default=0)
    htanksA = models.IntegerField(default=0)
    motorizedA = models.IntegerField(default=0)

    infantryD = models.IntegerField(default=0)
    hinfantryD = models.IntegerField(default=0)
    planesD = models.IntegerField(default=0)
    ltanksD = models.IntegerField(default=0)
    htanksD = models.IntegerField(default=0)
    motorizedD = models.IntegerField(default=0)

    infantryAS = models.IntegerField(default=0)
    hinfantryAS = models.IntegerField(default=0)
    planesAS = models.IntegerField(default=0)
    ltanksAS = models.IntegerField(default=0)
    htanksAS = models.IntegerField(default=0)
    motorizedAS = models.IntegerField(default=0)

    infantryDS = models.IntegerField(default=0)
    hinfantryDS = models.IntegerField(default=0)
    planesDS = models.IntegerField(default=0)
    ltanksDS = models.IntegerField(default=0)
    htanksDS = models.IntegerField(default=0)
    motorizedDS = models.IntegerField(default=0)

    def generateName(self):
        self.name = str(self.attacker.username) + " attacked city: " + str(self.cityD.city_name)

    def makeBattle(self):

        infantry = cityMap.models.Infantry.objects.get(id=1)
        hinfantry = cityMap.models.HInfantry.objects.get(id=1)
        ltanks = cityMap.models.LTanks.objects.get(id=1)
        htanks = cityMap.models.HTanks.objects.get(id=1)
        planes = cityMap.models.Planes.objects.get(id=1)
        motorized = cityMap.models.Motorized.objects.get(id=1)

        # --------------------------------------- #
        if self.infantryD >= self.infantryA:
            self.infantryDS = self.infantryA
            self.infantryAS = self.infantryA
            self.infantryD = self.infantryD - self.infantryA
            self.infantryA = 0
        else:
            self.infantryAS = self.infantryD
            self.infantryDS = self.infantryD
            self.infantryA = self.infantryA - self.infantryD
            self.infantryD = 0
        # --------------------------------------- #
        if self.hinfantryD >= self.hinfantryA:
            self.hinfantryDS = self.hinfantryA
            self.hinfantryAS = self.hinfantryA
            self.hinfantryD = self.hinfantryD - self.hinfantryA
            self.hinfantryA = 0
        else:
            self.hinfantryAS = self.hinfantryD
            self.hinfantryDS = self.hinfantryD
            self.hinfantryA = self.hinfantryA - self.hinfantryD
            self.hinfantryD = 0
        # -------------------------------------- #
        if self.planesD >= self.planesA:
            self.planesDS = self.planesA
            self.planesAS = self.planesA
            self.planesD = self.planesD - self.planesA
            self.planesA = 0
        else:
            self.planesAS = self.planesD
            self.planesDS = self.planesD
            self.planesA = self.planesA - self.planesD
            self.planesD = 0
        # --------------------------------------- #
        if self.ltanksD >= self.ltanksA:
            self.ltanksDS = self.ltanksA
            self.ltanksAS = self.ltanksA
            self.ltanksD = self.ltanksD - self.ltanksA
            self.ltanksA = 0
        else:
            self.ltanksAS = self.ltanksD
            self.ltanksDS = self.ltanksD
            self.ltanksA = self.ltanksA - self.ltanksD
            self.ltanksD = 0
        # --------------------------------------- #
        if self.htanksD >= self.htanksA:
            self.htanksDS = self.htanksA
            self.htanksAS = self.htanksA
            self.htanksD = self.htanksD - self.htanksA
            self.htanksA = 0
        else:
            self.htanksAS = self.htanksD
            self.htanksDS = self.htanksD
            self.htanksA = self.htanksA - self.htanksD
            self.htanksD = 0
        # --------------------------------------- #
        if self.motorizedD >= self.motorizedA:
            self.motorizedDS = self.motorizedA
            self.motorizedAS = self.motorizedA
            self.motorizedD = self.motorizedD - self.motorizedA
            self.motorizedA = 0
        else:
            self.motorizedAS = self.motorizedD
            self.motorizedDS = self.motorizedD
            self.motorizedA = self.motorizedA - self.motorizedD
            self.motorizedD = 0
        # --------------------------------------- #

        attackerPower = self.infantryA * infantry.attack + self.hinfantryA * hinfantry.attack + self.ltanksA * ltanks.attack + self.htanksA * htanks.attack + self.planesA * planes.attack + self.motorizedA * motorized.attack

        defenderPower = self.infantryD * infantry.attack + self.hinfantryD * hinfantry.attack + self.ltanksD * ltanks.attack + self.htanksD * htanks.attack + self.planesD * planes.attack + self.motorizedD * motorized.attack

        if attackerPower > defenderPower:
            self.infantryDS += self.infantryD
            self.hinfantryDS += self.hinfantryD
            self.planesDS += self.planesD
            self.ltanksDS += self.ltanksD
            self.htanksDS += self.htanksD
            self.motorizedDS += self.motorizedD

            self.infantryD = 0
            self.hinfantryD = 0
            self.planesD = 0
            self.ltanksD = 0
            self.htanksD = 0
            self.motorizedD = 0

            capacity = self.infantryA * infantry.capacity + self.hinfantryA * hinfantry.capacity + self.ltanksA * ltanks.capacity + self.htanksA * htanks.capacity + self.planesA * planes.capacity + self.motorizedA * motorized.capacity
            capacity = capacity / 3
            self.stolen_energy = capacity
            self.stolen_food = capacity
            self.stolen_minerals = capacity
        elif defenderPower == attackerPower:
            self.infantryAS += self.infantryA
            self.hinfantryAS += self.hinfantryA
            self.planesAS += self.planesA
            self.ltanksAS += self.ltanksA
            self.htanksAS += self.htanksA
            self.motorizedAS += self.motorizedA

            self.infantryDS += self.infantryD
            self.hinfantryDS += self.hinfantryD
            self.planesDS += self.planesD
            self.ltanksDS += self.ltanksD
            self.htanksDS += self.htanksD
            self.motorizedDS += self.motorizedD

            self.infantryA = 0
            self.hinfantryA = 0
            self.planesA = 0
            self.ltanksA = 0
            self.htanksA = 0
            self.motorizedA = 0

            self.infantryD = 0
            self.hinfantryD = 0
            self.planesD = 0
            self.ltanksD = 0
            self.htanksD = 0
            self.motorizedD = 0
        else:
            self.infantryAS += self.infantryA
            self.hinfantryAS += self.hinfantryA
            self.planesAS += self.planesA
            self.ltanksAS += self.ltanksA
            self.htanksAS += self.htanksA
            self.motorizedAS += self.motorizedA

            self.infantryDS += self.infantryD
            self.hinfantryDS += self.hinfantryD
            self.planesDS += self.planesD
            self.ltanksDS += self.ltanksD
            self.htanksDS += self.htanksD
            self.motorizedDS += self.motorizedD


class AllianceInvite(models.Model):
    sender = models.ForeignKey(User, related_name='senderair', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiverair', on_delete=models.CASCADE)
    alliance = models.ForeignKey(alliance.models.Alliance, related_name='receiver', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="alliance invite")
    created_date = models.DateTimeField(default=timezone.now)
    have_seen = models.BooleanField(default=False)

    def generateName(self):
        self.name = self.alliance.name + " invited by " + self.sender


class TradeRaport(models.Model):
    sender = models.ForeignKey(User, related_name='sendertr', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receivertr', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="trade report")
    city = models.ForeignKey(cityMap.models.CityOwned, related_name='citytr', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    have_seen = models.BooleanField(default=False)

    def generateName(self):
        self.name = self.sender.username + " make a trade with you"


class HelpRaport(models.Model):
    sender = models.ForeignKey(User, related_name='senderhr', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiverhr', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="help report")
    created_date = models.DateTimeField(default=timezone.now)
    city = models.ForeignKey(cityMap.models.CityOwned, related_name='cityhr', on_delete=models.CASCADE)
    have_seen = models.BooleanField(default=False)

    def generateName(self):
        self.name = "help to: " + str(self.sender.username) + " city: " + str(self.city)


class SpecialResourceRaport(models.Model):
    receiver = models.ForeignKey(User, related_name='receiversrr', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="resource report")
    created_date = models.DateTimeField(default=timezone.now)
    city = models.ForeignKey(cityMap.models.CityOwned, related_name='citysrr', on_delete=models.CASCADE)
    have_seen = models.BooleanField(default=False)

    def generateName(self):
        self.name = self.city.name + " special resource event"

