from rest_framework import viewsets
from .serializer import (
    CharacterSerializer,
    DmSerializer,
    PartySerializer,
    RelationSerializer,
    DesireSerializer,
    UserProfileSerializer,
    ArchetypeSerializer,
    EconomicSerializer,
)
from .models import (
    Characters,
    Dm,
    Party,
    Desires,
    Relations,
    UserProfile,
    Archetypes,
    EconomicStatus,
)
from .authentication.custom_permissions import IsOwnerOrAdmin, IsCharacterOwnerOrCreator,ReadOnly

# ! tene en cuenta por favor que estoy declarando todo en base al orden de importancia y aparicion


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrAdmin]


# ? de momento esto lo comentare, luego hare pruebas de rendimiento para ver si vale la pena o no
"""
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=user)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
"""
# ? por favor tene en cuenta esto para mas adelante


class DmViewSets(viewsets.ModelViewSet):
    queryset = Dm.objects.all()
    serializer_class = DmSerializer
    permission_classes = [IsOwnerOrAdmin]


class PartyViewSets(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsOwnerOrAdmin]


# ! OJO, acordate que tenemos dos campos extras, el creado y el dueño. hay que verificar que ambos puedan editar
class CharacterViewSets(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsCharacterOwnerOrCreator]

    def has_permission(self, request, view):
        if request.method == "DELETE":
            obj = self.get_object()
            return request.user == obj.creator
        return True

# * esto tiene permiso de solo escritura ya que esto cambia solo si hay una actualizacion en el reglamento del juego
class RelationViewSets(viewsets.ModelViewSet):
    queryset = Relations.objects.all()
    serializer_class = RelationSerializer
    permission_classes = [ReadOnly]
    


class DesireViewSets(viewsets.ModelViewSet):
    queryset = Desires.objects.all()
    serializer_class = DesireSerializer
    permission_classes = [ReadOnly]
    


class EconomicViewSets(viewsets.ModelViewSet):
    queryset = EconomicStatus.objects.all()
    serializer_class = EconomicSerializer
    permission_classes = [ReadOnly]
    


class ArchetypeSerializer(viewsets.ModelViewSet):
    queryset = Archetypes.objects.all()
    serializer_class = ArchetypeSerializer
    permission_classes = [ReadOnly]
    


# clase principal que determina si uno es admin o es propietario

# Create your views here.
# class UserViewSets(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
