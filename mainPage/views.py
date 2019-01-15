from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, SupportTicket
from .models import Server
from .models import CityPositions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ExtendedUserCreationForm, CommentForm, SupportTicketForm
from django.http import HttpResponse
from cityMap.models import CityOwned, Housing, Farms, PowerPlant, Mines, Roads, TownHall, Barracks
from cityMap.models import Infantry, HInfantry, LTanks, HTanks, Motorized, Planes
from django.contrib.admin.views.decorators import staff_member_required

def page_not_found_view(request):
    return render(request, '404.html')

@staff_member_required
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


@staff_member_required
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
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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


@login_required(login_url=main_page)
def show_support_employee(request):
    if request.user.groups.filter(name='Support').exists():
        tickets = SupportTicket.objects.filter(have_been_taken=False).order_by('created_date')
        your_tickets = SupportTicket.objects.filter(have_been_taken_by=request.user).order_by('created_date')
        return render(request, 'supportEmployee.html', {'tickets': tickets, 'your_tickets': your_tickets})
    else:
        return redirect(main_page)


@login_required(login_url=main_page)
def show_employee_ticket_details(request, id_of_ticket):
    if request.user.groups.filter(name='Support').exists():
        ticket = SupportTicket.objects.get(id=id_of_ticket)
        if ticket.author == request.user:
            form = CommentForm()
            if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.author = request.user
                    form.save()
                    ticket.comments.add(form)
                    ticket.have_been_taken = True
                    ticket.have_been_taken_by = request.user
                    ticket.save()
                    form = CommentForm()

            return render(request, 'ticketDetailEmployee.html', {'ticket': ticket, 'form': form})
        else:
            return redirect(main_page)


def show_support(request):
    form = SupportTicketForm()
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Support').exists():
            return redirect("supportEmployee/")
        else:
            tickets = SupportTicket.objects.filter(author=request.user).order_by('created_date')
            if request.method == 'POST':
                form = SupportTicketForm(request.POST)
                if form.is_valid():
                    form_backup = form
                    form = form.save(commit=False)
                    form.author = request.user
                    form.question_type = form_backup.cleaned_data['question_type']
                    form.save()
                    id_of_ticket = form.id
                    return redirect(str(id_of_ticket) + "/")
            return render(request, 'support.html', {'form': form, 'tickets': tickets})
    else:
        tickets = None
        form = None
        return render(request, 'support.html', {'form': form, 'tickets': tickets})


@login_required(login_url=main_page)
def show_ticket_details(request, id_of_ticket):
    ticket = SupportTicket.objects.get(id=id_of_ticket)
    if ticket.author == request.user:
        form = CommentForm()
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.save()
                ticket.comments.add(form)
                ticket.save()
                form = CommentForm()

        return render(request, 'ticketDetail.html', {'ticket': ticket, 'form': form})
    else:
        return redirect(main_page)


def show_faq(request):
    return render(request, 'faq.html')
