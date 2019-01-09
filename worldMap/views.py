from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import cityMap.models
from alliance.models import Alliance
from mainPage.models import Profile
from django.contrib.auth.models import User

from mainPage.views import main_page
from .models import Attack, Support
from cityMap.models import CityOwned
from rest_framework.utils import json
import math
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.


@login_required(login_url=main_page)
def main_page_map(request):
    city_list = cityMap.models.CityOwned.objects.all()
    attacks = Attack.objects.all()
    supports = Support.objects.all()
    profil = Profile.objects.get(user=request.user)
    return render(request, 'indexWorldMap.html', {'city_list': city_list, 'attacks': attacks, 'supports': supports, 'profil': profil})


@login_required(login_url=main_page)
def city_detail_info(request, id_of_city):
    city = cityMap.models.CityOwned.objects.get(id=id_of_city)
    profil = Profile.objects.get(user=request.user)
    profil_owner = Profile.objects.get(user=city.city_owner)
    same_alliance = 0
    if profil.alliance is not None:
        if profil.alliance == profil_owner.alliance:
            same_alliance = 1

    if city.city_owner == request.user:
        same_alliance = 1

    return render(request, 'cityDetailInfo.html', {'city': city, 'same_alliance': same_alliance})


@login_required(login_url=main_page)
def city_attack(request, id_of_city):
    attack_succesfull = 0
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        attack_correct = data['attack_correct']
        if attack_correct == 1:
            attacker_city = CityOwned.objects.get(id=data['attacking_city'])
            defender_city = CityOwned.objects.get(id=id_of_city)
            attack = Attack(attacker=attacker_city,
                            defender=defender_city, infantry=data['infantry'],
                            hinfantry=data['hinfantry'], planes=data['planes'], ltanks=data['ltanks'],
                            htanks=data['htanks'], motorized=data['motorized'])
            distance_between_citys = math.sqrt((defender_city.pos_x - attacker_city.pos_x)**2 + (defender_city.pos_y - attacker_city.pos_y)**2)
            attack.arrive = timezone.now() + timezone.timedelta(seconds=int(distance_between_citys))
            attack.save()
            attack_succesfull = 1
            return JsonResponse({'attack_succesfull': attack_succesfull})
        return JsonResponse({'attack_succesfull': attack_succesfull})
    return render(request, 'attacks.html', {'id_of_city': id_of_city})


@login_required(login_url=main_page)
def city_support(request, id_of_city):
    support_succesfull = 0
    profil = Profile.objects.get(user=request.user)
    city = cityMap.models.CityOwned.objects.get(id=id_of_city)
    profil_owner = Profile.objects.get(user=city.city_owner)
    if profil.alliance == profil_owner.alliance or city.city_owner == request.user:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            support_correct = data['support_correct']
            if support_correct == 1:
                support_city = CityOwned.objects.get(id=data['support_city'])
                defender_city = CityOwned.objects.get(id=id_of_city)
                support = Support(support=support_city,
                                defender=defender_city, infantry=data['infantry'],
                                hinfantry=data['hinfantry'], planes=data['planes'], ltanks=data['ltanks'],
                                htanks=data['htanks'], motorized=data['motorized'])
                distance_between_citys = math.sqrt((defender_city.pos_x - support_city.pos_x)**2 + (defender_city.pos_y - support_city.pos_y)**2)
                support.arrive = timezone.now() + timezone.timedelta(seconds=int(distance_between_citys))
                support.save()
                support_succesfull = 1
                return JsonResponse({'support_succesfull': support_succesfull})
            return JsonResponse({'support_succesfull': support_succesfull})
        return render(request, 'supportWM.html', {'id_of_city': id_of_city})
    return render(request, 'supportWM.html', {'id_of_city': id_of_city})


@login_required(login_url=main_page)
def city_owner_detail_info(request, id_of_city, id_of_user):
    user = User.objects.get(id=id_of_user)
    citys = cityMap.models.CityOwned.objects.filter(city_owner=user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetailInfo.html', {'user': user, 'profil': profil, 'citys': citys})
