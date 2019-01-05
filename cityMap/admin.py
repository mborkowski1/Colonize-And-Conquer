from django.contrib import admin
from .models import CityOwned, Housing, Farms, PowerPlant, Mines, Roads, TownHall, Barracks
from .models import Infantry, HInfantry, LTanks, HTanks, Motorized, Planes
# Register your models here.


admin.site.register(CityOwned)

admin.site.register(Barracks)
admin.site.register(TownHall)
admin.site.register(Roads)
admin.site.register(Mines)
admin.site.register(PowerPlant)
admin.site.register(Farms)
admin.site.register(Housing)

admin.site.register(Infantry)
admin.site.register(HInfantry)
admin.site.register(LTanks)
admin.site.register(HTanks)
admin.site.register(Motorized)
admin.site.register(Planes)
