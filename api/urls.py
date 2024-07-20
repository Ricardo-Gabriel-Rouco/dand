from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSets)
router.register(r'dm', views.DmViewSets)
router.register(r'characters', views.CharacterViewSets)
router.register(r'party', views.PartyViewSets)

urlpatterns=[
  path('', include(router.urls))
]
