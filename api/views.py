from rest_framework import viewsets

from .serializer import UserSerializer, CharacterSerializer, DmSerializer, PartySerializer, RelationSerializer, DesireSerializer, UserProfileSerializer
from .models import User, Characters, Dm, Party, Desires, Relations, UserProfile

# Create your views here.
# class UserViewSets(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CharacterViewSets(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer


class DmViewSets(viewsets.ModelViewSet):
    queryset = Dm.objects.all()
    serializer_class = DmSerializer


class PartyViewSets(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class RelationViewSets(viewsets.ModelViewSet):
    queryset = Relations.objects.all()
    serializer_class = RelationSerializer

class DesireWiewSets(viewsets.ModelViewSet):
    queryset = Desires.objects.all()
    serializer_class = DesireSerializer
    
