from django.db import models
from  django.contrib.auth.models import User
from .validations  import validateLevel, validateArmorClass
from model_utils.models import TimeStampedModel, SoftDeletableModel

partyChoices = [
    ("D&D5th", "D&D5th",),
    ("GoodSociety", "Good Society")
]
partyStatus = [
    ("RD", "READY"),
    ("OG", "ONGOING"),
    ("ED", "ENDED")
]

# Create your models here.


class UserProfile(TimeStampedModel, SoftDeletableModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=150, null=True, blank=True)
    novice = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    characters = models.ForeignKey('Characters', on_delete=models.CASCADE, blank=True, null=True)
    dmId = models.OneToOneField('Dm', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.id} {self.nickname} {self.characters} {self.novice} {self.dmId}"

class Dm(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, null=False, blank=False)
    dmParty = models.ManyToManyField('Party')

class Party(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, null=False, blank=False)
    partySystem = models.CharField(max_length=150,choices=partyChoices, blank=False, null=False)
    partyState = models.CharField(max_length=150,choices=partyStatus, blank=False, null=False)
    partyIntro = models.TextField(blank=False, null=False)
    partyRules = models.TextField(blank=False, null=False)
    members = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} {self.name} {self.partySystem} {self.partyState} {self.partyIntro} {self.partyRules} {self.members}"

class Characters(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, blank=False, null=False)
    nickname = models.CharField(max_length=150)
    level = models.IntegerField(validators=[validateLevel])
    characterClass = models.CharField(max_length=150, blank=False, null=False)
    armor_class = models.IntegerField(default=10, validators=[validateArmorClass])
    modifiers = models.JSONField(null=False, blank=False)
    healthPoints = models.IntegerField(blank=False, null=False, default=1)
    image = models.CharField(max_length=500,blank=True, null=True)
    # Pure Good Society
    desires = models.ForeignKey("Desires", on_delete=models.PROTECT, blank=True, null=True)
    relationships = models.ForeignKey("Relations", on_delete=models.PROTECT, blank=True, null=True)
    economic_status = models.ForeignKey("EconomicStatus", on_delete=models.PROTECT, blank=True, null=True)
    reputation = models.JSONField(blank=True, null=True)
    archetype = models.ForeignKey("Archetypes",on_delete=models.PROTECT ,blank=True, null=True)
    tokens = models.IntegerField(default=3, blank=True, null=True)
    def __str__(self):
        return f"{self.name}{self.nickname} {self.id} {self.level} {self.modifiers}" 
    #aca termina good society dentro de characters

# esto es puro good society
class Desires(TimeStampedModel, SoftDeletableModel):
    type = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.id} {self.type} {self.description}" 

class Relations(TimeStampedModel, SoftDeletableModel):
    type = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.id} {self.type} {self.description}"
    
class EconomicStatus(TimeStampedModel, SoftDeletableModel):
    type = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.id} {self.type} {self.description}"
    
class Archetypes(TimeStampedModel, SoftDeletableModel):
    type = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.id} {self.type} {self.description}"