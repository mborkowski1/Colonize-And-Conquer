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
def add_forum_post(request, id_of_alliance):
    profile = Profile.objects.get(user=request.user)
    if profile.alliance is not None:
        if profile.alliance.id == id_of_alliance:
            if request.method == 'POST':
                data = json.loads(request.body.decode('utf-8'))
                id_of_topic = data['id_of_topic']
                text = data['text']
                new_post = PostForum(text=text, author=request.user)
                new_post.save()
                topic = Topic.objects.get(id=id_of_topic)
                topic.posts.add(new_post)
                topic.save()
                return JsonResponse({'succesfull': 1})
            else:
                return JsonResponse({'succesfull': 0})
        else:
            return JsonResponse({'succesfull': 0})
    else:
        return JsonResponse({'succesfull': 0})


@login_required(login_url=main_page)
def add_forum_topic(request, id_of_alliance):
    profile = Profile.objects.get(user=request.user)
    if profile.alliance is not None:
        if profile.alliance.id == id_of_alliance:
            if request.method == 'POST':
                data = json.loads(request.body.decode('utf-8'))
                id_of_sub_forum = data['id_of_sub_forum']
                title = data['title']
                new_topic = Topic(title=title)
                new_topic.save()
                sub_forum = SubForum.objects.get(id=id_of_sub_forum)
                sub_forum.topics.add(new_topic)
                sub_forum.save()
                return JsonResponse({'succesfull': 1})
            else:
                return JsonResponse({'succesfull': 0})
        else:
            return JsonResponse({'succesfull': 0})
    else:
        return JsonResponse({'succesfull': 0})


@login_required(login_url=main_page)
def add_forum_sub_forum(request, id_of_alliance):
    profile = Profile.objects.get(user=request.user)
    if profile.alliance is not None:
        alliance = Alliance.objects.get(id=profile.alliance.id)
        if alliance.creator == request.user or alliance.vice_creator == request.user:
            if request.method == 'POST':
                data = json.loads(request.body.decode('utf-8'))
                id_of_forum = data['id_of_forum']
                title = data['title']
                new_subforum = SubForum(title=title)
                new_subforum.save()
                forum = Forum.objects.get(id=id_of_forum)
                forum.sub_forums.add(new_subforum)
                forum.save()
                return JsonResponse({'succesfull': 1})
            else:
                return JsonResponse({'succesfull': 0})
        else:
            return JsonResponse({'succesfull': 0})
    else:
        return JsonResponse({'succesfull': 0})


@login_required(login_url=main_page)
def show_alliance_forum(request, id_of_alliance):
    return render(request, 'allianceForum.html', {'id_of_alliance': id_of_alliance})


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
