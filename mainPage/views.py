from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .models import Server
from .models import CityPositions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ExtendedUserCreationForm, CommentForm, SupportTicketForm
from django.http import HttpResponse
#from cityMap.models import CityOwned, Housing, Farms, PowerPlant, Mines, Roads, TownHall, Barracks
#from cityMap.models import Infantry, HInfantry, LTanks, HTanks, Motorized, Planes


def generate_basic_tables(request):
    building = Barracks()
    building.save()
    building = TownHall()
    building.save()
    building = Roads()
    building.save()
    building = Mines()
    building.save()
    building = PowerPlant()
    building.save()
    building = Farms()
    building.save()
    building = Housing()
    building.save()
    building = Infantry()
    building.save()
    building = HInfantry()
    building.save()
    building = LTanks()
    building.save()
    building = HTanks()
    building.save()
    building = Motorized()
    building.save()
    building = Planes()
    building.save()
    return HttpResponse('Generated tables without problems.')


def fill_village_pos_table(request):
    posx = 1
    posy = 1
    position = CityPositions(village_x=posx, village_y=posy)
    position.save()
    for i in range(1, 1000):
        if posx + 100 > 1000:
            posx = 1
            if posy + 100 > 1000:
                break
            else:
                posy += 100
        else:
            posx += 100

        position = CityPositions(village_x=posx, village_y=posy)
        position.save()

        if posy == 901 and posx == 901:
            break

    return HttpResponse('Generated city positions without problems.')


def main_page(request):
    servers = Server.objects.all()
    if request.method == 'POST':
        if 'SignUpForm' in request.POST:
            form = ExtendedUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('miasto/')
            login_form = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'login_form': login_form, 'servers': servers})

        elif 'LogInForm' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            form = ExtendedUserCreationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                servers = Server.objects.all()
                return render(request, 'index.html',
                              {'servers': servers, 'posts': posts, 'form': form, 'login_form': login_form})
            else:
                return render(request, 'index.html', {'posts': posts, 'form': form, 'login_form': login_form})

        elif 'LogOutForm' in request.POST:
            logout(request)
            form = ExtendedUserCreationForm()
            login_form = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'login_form': login_form})

    else:
        user = request.user.is_authenticated
        if user:
            login_form = AuthenticationForm(data=request.POST)
            form = ExtendedUserCreationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html',
                          {'servers': servers, 'posts': posts, 'form': form, 'login_form': login_form})
        else:
            form = ExtendedUserCreationForm()
            login_form = AuthenticationForm()
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'index.html', {'posts': posts, 'form': form, 'login_form': login_form})


def show_article_details(request, id_of_article):
    post = Post.objects.get(id=id_of_article)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            post.comments.add(form)
            post.save()
            form = CommentForm()

    return render(request, 'articleDetail.html', {'post': post, 'form': form})


def show_forum(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum.html', {'posts': posts})


def show_support(request):
    form = SupportTicketForm()
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)

        if form.is_valid():
            formm = form.save(commit=False)
            formm.author = request.user
            formm.question_type = form.cleaned_data['question_type']
            formm.save()

    return render(request, 'support.html', {'form': form})


def show_faq(request):
    return render(request, 'faq.html')
