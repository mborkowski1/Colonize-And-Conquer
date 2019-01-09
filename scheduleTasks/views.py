from django.shortcuts import render
import cityMap.models
from django.http import HttpResponse
from worldMap.models import Attack, Support
import time
from raports.models import BattleRaport, HelpRaport
from cityMap.models import CityOwned
# Create your views here.


def dodaj_surowce(request):
    city_list = cityMap.models.CityOwned.objects.all()
    for city in city_list:
        roads_percent = city.roads / 10
        city.food += city.farms * 10 + (city.farms * 10 * roads_percent)
        city.electricity += city.power_plant * 10 + (city.power_plant * 10 * roads_percent)
        city.ore += city.mines * 10 + (city.mines * 10 * roads_percent)
        city.save()

    return HttpResponse('Updated Resources')


def zaktualizuj_wsparcie(request):
    supports = Support.objects.all()
    for support in supports:
        defender_city = CityOwned.objects.get(id=support.defender.id)
        defender_city.infantry += support.infantry
        defender_city.hinfantry += support.hinfantry
        defender_city.planes += support.planes
        defender_city.ltanks += support.ltanks
        defender_city.htanks += support.htanks
        defender_city.motorized += support.motorized
        defender_city.save()

        raport = HelpRaport(sender=support.support.city_owner, receiver=support.defender.city_owner,
                            city=support.defender)
        raport.generateName()

        raport.infantry = support.infantry
        raport.hinfantry = support.hinfantry
        raport.planes = support.planes
        raport.ltanks = support.ltanks
        raport.htanks = support.htanks
        raport.motorized = support.motorized

        raport.save()
        support.delete()

    return HttpResponse('Deleted old supports')


def zaktualizuj_ataki(request):
    attacks = Attack.objects.all()
    for attack in attacks:
        if attack.arrive.timestamp() < int(time.time()):
            raport = BattleRaport(attacker=attack.attacker.city_owner, defender=attack.defender.city_owner,
                                  cityA=attack.attacker, cityD=attack.defender)
            # get citys to update later
            attacker_city = CityOwned.objects.get(id=attack.attacker.id)
            defender_city = CityOwned.objects.get(id=attack.defender.id)
            # units attacker
            raport.infantryA = attack.infantry
            raport.hinfantryA = attack.hinfantry
            raport.planesA = attack.planes
            raport.ltanksA = attack.ltanks
            raport.htanksA = attack.htanks
            raport.motorizedA = attack.motorized
            # units defender
            raport.infantryD = defender_city.infantry
            raport.hinfantryD = defender_city.hinfantry
            raport.planesD = defender_city.planes
            raport.ltanksD = defender_city.ltanks
            raport.htanksD = defender_city.htanks
            raport.motorizedD = defender_city.motorized
            # make battle
            raport.generateName()
            raport.makeBattle()

            if defender_city.food > raport.stolen_food:
                defender_city.food -= raport.stolen_food
                attacker_city.food += raport.stolen_food
            else:
                attacker_city.food += defender_city.food
                raport.stolen_food = defender_city.food
                defender_city.food = 0

            if defender_city.electricity > raport.stolen_energy:
                defender_city.electricity -= raport.stolen_energy
                attacker_city.electricity += raport.stolen_energy
            else:
                attacker_city.electricity += defender_city.electricity
                raport.stolen_energy = defender_city.electricity
                defender_city.electricity = 0

            if defender_city.ore > raport.stolen_minerals:
                defender_city.ore -= raport.stolen_minerals
                attacker_city.ore += raport.stolen_minerals
            else:
                attacker_city.ore += defender_city.ore
                raport.stolen_minerals = defender_city.ore
                defender_city.ore = 0

            raport.save()
            # update city army
            # attacker
            attacker_city.infantry -= raport.infantryAS
            attacker_city.hinfantry -= raport.hinfantryAS
            attacker_city.planes -= raport.planesAS
            attacker_city.ltanks -= raport.ltanksAS
            attacker_city.htanks -= raport.htanksAS
            attacker_city.motorized -= raport.motorizedAS
            # units that survived
            attacker_city.infantry += raport.infantryA - raport.infantryAS
            attacker_city.hinfantry += raport.hinfantryA - raport.hinfantryAS
            attacker_city.planes += raport.planesA - raport.planesAS
            attacker_city.ltanks += raport.ltanksA - raport.ltanksAS
            attacker_city.htanks += raport.htanksA - raport.htanksAS
            attacker_city.motorized += raport.motorizedA - raport.motorizedAS

            attacker_city.save()
            # defender
            defender_city.infantry -= raport.infantryDS
            defender_city.hinfantry -= raport.hinfantryDS
            defender_city.planes -= raport.planesDS
            defender_city.ltanks -= raport.ltanksDS
            defender_city.htanks -= raport.htanksDS
            defender_city.motorized -= raport.motorizedDS

            defender_city.save()
            # delete attack order
            attack.delete()

    return HttpResponse('Deleted old attacks')
