from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mainPage.views import main_page
from .models import BattleRaport, AllianceInvite, HelpRaport, SpecialResourceRaport, TradeRaport
from alliance.models import Alliance
from mainPage.models import Profile
from django.db.models import Q


# Create your views here.


@login_required(login_url=main_page)
def raport_page(request):
    battleraports = BattleRaport.objects.filter(Q(defender=request.user) | Q(attacker=request.user)).order_by('created_date')
    alliancereports = AllianceInvite.objects.filter(receiver=request.user).order_by('created_date')
    helpraports = HelpRaport.objects.filter(receiver=request.user).order_by('created_date')
    specialresourceraports = SpecialResourceRaport.objects.filter(receiver=request.user).order_by('created_date')
    tradeeraports = TradeRaport.objects.filter(receiver=request.user).order_by('created_date')
    return render(request, 'indexRaports.html',
                  {'battleraports': battleraports, 'alliancereports': alliancereports, 'helpraports': helpraports,
                   'specialresourceraports': specialresourceraports, 'tradeeraports': tradeeraports})


@login_required(login_url=main_page)
def raport_detail_page(request, id_of_raport, type_of_raport):
    if type_of_raport == 0:
        raport = BattleRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
        infantryD = raport.infantryD + raport.infantryDS
        hinfantryD = raport.hinfantryD + raport.hinfantryDS
        motorizedD = raport.motorizedD + raport.motorizedDS
        ltanksD = raport.ltanksD + raport.ltanksDS
        htanksD = raport.htanksD + raport.htanksDS
        planesD = raport.planesD + raport.planesDS

        infantryA = raport.infantryA + raport.infantryAS
        hinfantryA = raport.hinfantryA + raport.hinfantryAS
        motorizedA = raport.motorizedA + raport.motorizedAS
        ltanksA = raport.ltanksA + raport.ltanksAS
        htanksA = raport.htanksA + raport.htanksAS
        planesA = raport.planesA + raport.planesAS

        return render(request, 'raportDetail.html',
                      {'infantryD': infantryD, 'hinfantryD': hinfantryD, 'motorizedD': motorizedD, 'ltanksD': ltanksD,
                       'htanksD': htanksD, 'planesD': planesD, 'infantryA': infantryA, 'hinfantryA': hinfantryA,
                       'motorizedA': motorizedA, 'ltanksA': ltanksA, 'htanksA': htanksA, 'planesA': planesA,
                       'raport': raport, 'type_of_raport': type_of_raport})
    elif type_of_raport == 1:
        raport = AllianceInvite.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 2:
        raport = HelpRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 3:
        raport = SpecialResourceRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()
    elif type_of_raport == 4:
        raport = TradeRaport.objects.get(id=id_of_raport)
        raport.have_seen = True
        raport.save()

    return render(request, 'raportDetail.html', {'raport': raport, 'type_of_raport': type_of_raport})


@login_required(login_url=main_page)
def accept_alliance_invite(request, id_of_raport):
    raport = AllianceInvite.objects.get(id=id_of_raport)
    user = request.user
    if raport.receiver == user:
        alliance = Alliance.objects.get(id=raport.alliance.id)
        alliance.members.add(user)
        alliance.save()
        profil = Profile.objects.get(user=user)
        profil.alliance = alliance
        profil.save()
        return redirect('../../../../../../../../../sojusz/')
    else:
        return redirect('../../../../../../../../../')
