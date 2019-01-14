from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from mainPage.views import main_page
from projektNaChmureDJango import settings
from .models import Premium, Tranzakcja
from mainPage.models import Profile
from django.utils import timezone
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm


@csrf_exempt
def payment_done(request, payment_id):
    return render(request, 'done.html')


@csrf_exempt
def payment_canceled(request, payment_id):
    return render(request, 'canceled.html')


def payment_process(request, typPremium):
    #if request.method == 'POST':
    user = request.user
    profile = Profile.objects.get(user=request.user)
    profile.is_premium = True
    profile.until_premium = timezone.now()
    #profile.until_premium = timezone.now() + timedelta(days = 30)
    profile.save()
    tranzakcja = Tranzakcja(buyer=user, type_of_premium=typPremium)
    tranzakcja.save()
    
    host = request.get_host()
    premium = Premium.objects.get(id=1)
    tranzakcja_id = tranzakcja.id
    tranzakcja = Tranzakcja.objects.get(id=tranzakcja_id)
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": '%.2F' % premium.price_one_month,
        "item_name": "Premium",
        "invoice": str(tranzakcja_id),
        'currency_code': 'USD',
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('payment:done', kwargs={'payment_id': tranzakcja_id})),
        "cancel_return": request.build_absolute_uri(reverse('payment:canceled', kwargs={'payment_id': tranzakcja_id})),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "process.html", {'tranzakcja': tranzakcja, 'form': form})


@login_required(login_url=main_page)
def premium_page(request):
    premiumOptions = Premium.objects.get(id=1)
    return render(request, 'indexPremium.html', {'premiumOptions': premiumOptions})


@login_required(login_url=main_page)
def premium_platnosc(request):
    user = request.user
    return render(request, 'process.html')


@login_required(login_url=main_page)
def premium_history(request):
    user = request.user
    tranzakcje = Tranzakcja.objects.all().filter(buyer=user)
    return render(request, 'platnosci.html', {'tranzakcje': tranzakcje})
