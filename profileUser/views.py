from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mainPage.views import main_page
from .forms import EditEmailForm, EditProfileForm
from mainPage.models import Profile
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


@login_required(login_url=main_page)
def profile_page(request):
    user = request.user
    profil = Profile.objects.get(user=user)
    return render(request, 'indexProfileUser.html', {'user': user, 'profil': profil})


@login_required(login_url=main_page)
def profilowe_page(request):

    profil = Profile.objects.get(user=request.user)
    profile_form = EditProfileForm(instance=profil)
    email_form = EditEmailForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'change_profil' in request.POST:
            profile_form = EditProfileForm(request.POST, request.FILES, instance=profil)
            if profile_form.is_valid():
                profile_form.save()
                return render(request, 'profileProfileUser.html',
                              {'profile_form': profile_form, 'profil': profil, 'email_form': email_form,
                               'password_form': password_form})
            return render(request, 'profileProfileUser.html',
                          {'profile_form': profile_form, 'profil': profil, 'email_form': email_form,
                           'password_form': password_form})

        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(data=request.POST, user=request.user)
            if password_form.is_valid():
                password_form.save()
                return redirect('../../')
            return render(request, 'profileProfileUser.html',
                          {'profile_form': profile_form, 'profil': profil, 'email_form': email_form,
                           'password_form': password_form})

        elif 'change_email' in request.POST:
            email_form = EditEmailForm(data=request.POST, instance=request.user)
            if email_form.is_valid():
                email_form.save()
                return render(request, 'profileProfileUser.html',
                              {'profile_form': profile_form, 'profil': profil, 'email_form': email_form,
                               'password_form': password_form})
            return render(request, 'profileProfileUser.html',
                          {'profile_form': profile_form, 'profil': profil, 'email_form': email_form,
                           'password_form': password_form})
    else:
        return render(request, 'profileProfileUser.html',
                      {'profile_form': profile_form, 'profil': profil, 'email_form': email_form,
                       'password_form': password_form})
