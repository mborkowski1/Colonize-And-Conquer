from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from mainPage.views import main_page
from .models import Alliance, SubForum, Forum, Topic, PostForum
from mainPage.models import Profile
from django.contrib.auth.models import User
from .forms import CreateAllianceForm, CreateAllianceInviteForm
from django.utils import timezone
from rest_framework.utils import json


@login_required(login_url=main_page)
def invite_to_your_alliance(request):
    profile = Profile.objects.get(user=request.user)
    if profile.alliance is not None:
        alliance = Alliance.objects.get(id=profile.alliance.id)
        if alliance.creator == request.user or alliance.vice_creator == request.user:
            form = CreateAllianceInviteForm()
            if request.method == 'POST':
                form = CreateAllianceInviteForm(request.POST)
                if form.is_valid():
                    form_edit = form.save(commit=False)
                    form_edit.sender = request.user
                    form_edit.alliance = alliance
                    form_edit.created_date = timezone.now()
                    form_edit.save()
                    form = CreateAllianceInviteForm()
                    return render(request, 'inviteAlliance.html', {'form': form})
                return render(request, 'inviteAlliance.html', {'form': form})
            return render(request, 'inviteAlliance.html', {'form': form})
        else:
            return redirect('../')
    else:
        return redirect('../')


@login_required(login_url=main_page)
def edit_your_alliance(request):
    profile = Profile.objects.get(user=request.user)
    if profile.alliance is not None:
        alliance = Alliance.objects.get(id=profile.alliance.id)
        if alliance.creator == request.user or alliance.vice_creator == request.user:
            form = CreateAllianceForm(instance=alliance)
            if request.method == 'POST':
                form = CreateAllianceForm(request.POST, request.FILES)
                if form.is_valid():
                    alliance_edit = form.save(commit=False)
                    alliance.name = alliance_edit.name
                    alliance.alliance_bio = alliance_edit.alliance_bio
                    alliance.alliance_logo = alliance_edit.alliance_logo
                    alliance.save()
                    form = CreateAllianceForm(instance=alliance)
                    return render(request, 'editAlliance.html', {'form': form})
                return render(request, 'editAlliance.html', {'form': form})
            return render(request, 'editAlliance.html', {'form': form})
        else:
            return redirect('../')
    else:
        return redirect('../')


@login_required(login_url=main_page)
def show_your_alliance(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.alliance is not None:
        alliance = Alliance.objects.get(id=profile.alliance.id)
        return render(request, 'indexAlliance.html', {'alliance': alliance})
    else:
        if request.method == 'POST':
            form = CreateAllianceForm(request.POST, request.FILES)
            if form.is_valid():
                alliance = form.save(commit=False)
                alliance.creator = request.user
                alliance.save()
                alliance.members.add(request.user)
                alliance.save()
                profile.alliance = alliance
                profile.save()
                return render(request, 'indexAlliance.html', {'alliance': alliance})
            alliance = 1
            return render(request, 'indexAlliance.html', {'form': form, 'alliance': alliance})
        alliance = 1
        form = CreateAllianceForm()
        return render(request, 'indexAlliance.html', {'form': form, 'alliance': alliance})


@login_required(login_url=main_page)
def alliance_list_page(request):
    alliances = Alliance.objects.all()
    return render(request, 'allianceList.html', {'alliances': alliances})


@login_required(login_url=main_page)
def alliance_detail_page(request, id_of_alliance):
    alliance = Alliance.objects.get(id=id_of_alliance)
    return render(request, 'allianceDetail.html', {'alliance': alliance})


@login_required(login_url=main_page)
def user_detail_page(request, id_of_alliance, id_of_user):
    user = User.objects.get(id=id_of_user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetail.html', {'user': user, 'profil': profil})


@login_required(login_url=main_page)
def user_your_alliance_detail_page(request, id_of_user):
    user = User.objects.get(id=id_of_user)
    profil = Profile.objects.get(user=user)
    return render(request, 'userDetail.html', {'user': user, 'profil': profil})
