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

