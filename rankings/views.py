from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
import cityMap
from mainPage.models import Profile
from mainPage.views import main_page


@login_required(login_url=main_page)
def ranking_page(request):
    return render(request, 'rankings.html')


@login_required(login_url=main_page)
def user_city_detail_info(request, id_of_user, id_of_city):
    city = cityMap.models.CityOwned.objects.get(id=id_of_city)
    return render(request, 'cityDetailInfoR.html', {'city': city})


@login_required(login_url=main_page)
def user_detail_info(request, id_of_user):
    user = User.objects.get(id=id_of_user)
    citys = cityMap.models.CityOwned.objects.filter(city_owner=user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetailInfoR.html', {'user': user, 'profil': profil, 'citys': citys})
