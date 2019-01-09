from django.contrib import admin
from .models import BattleRaport, AllianceInvite, TradeRaport, HelpRaport, SpecialResourceRaport

# Register your models here.
admin.site.register(BattleRaport)
admin.site.register(AllianceInvite)
admin.site.register(TradeRaport)
admin.site.register(HelpRaport)
admin.site.register(SpecialResourceRaport)