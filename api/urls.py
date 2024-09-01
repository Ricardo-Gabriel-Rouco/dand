from django.urls import path, include
from rest_framework import routers
from api import views
from .authentication import urls as auth_urls

router = routers.DefaultRouter()
router.register(r'profile', views.UserProfileViewSets)
router.register(r'dm', views.DmViewSets)
router.register(r'characters', views.CharacterViewSets)
router.register(r'party', views.PartyViewSets)
router.register(r'desires', views.DesireWiewSets, basename="desires")
router.register(r'relations', views.RelationViewSets, basename="relations")


urlpatterns=[
  path('', include(router.urls)),
  path('auth/', include(auth_urls))
]
