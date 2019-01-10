from rest_framework import routers
from cityMap.viewsets import CityOwnedViewSet, HousingViewSet, FarmsViewSet, PowerPlantViewSet, MinesViewSet
from cityMap.viewsets import HInfantryViewSet, InfantryViewSet, LTanksViewSet, HTanksViewSet, MotorizedViewSet
from cityMap.viewsets import PlanesViewSet, BarracksViewSet, TownHallViewSet, RoadsViewSet
from alliance.viewsets import AllianceViewSet, ForumViewSet, SubForumViewSet, TopicViewSet, PostForumViewSet
from mainPage.viewsets import UserViewSet, ProfileViewSet, CityPositionsViewSet, ServerViewSet

router = routers.DefaultRouter()
router.register(r'city', CityOwnedViewSet)
router.register(r'housing', HousingViewSet)
router.register(r'farms', FarmsViewSet)
router.register(r'powerPlant', PowerPlantViewSet)
router.register(r'mines', MinesViewSet)
router.register(r'hInfantry', HInfantryViewSet)
router.register(r'infantry', InfantryViewSet)
router.register(r'lTanks', LTanksViewSet)
router.register(r'hTanks', HTanksViewSet)
router.register(r'motorized', MotorizedViewSet)
router.register(r'planes', PlanesViewSet)
router.register(r'barracks', BarracksViewSet)
router.register(r'townHall', TownHallViewSet)
router.register(r'roads', RoadsViewSet)
router.register(r'alliance', AllianceViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'user', UserViewSet)
router.register(r'cityPosition', CityPositionsViewSet)
router.register(r'server', ServerViewSet)

router.register(r'forum', ForumViewSet)
router.register(r'subForum', SubForumViewSet)
router.register(r'topic', TopicViewSet)
router.register(r'postForum', PostForumViewSet)


