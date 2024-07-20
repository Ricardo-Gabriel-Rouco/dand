from django.db import models
from django.core.exceptions import ValidationError
from model_utils.models import TimeStampedModel, SoftDeletableModel

partyChoices = [
    ("D&D5th", "D&D5th")
]
partyStatus = [
    ("RD", "READY"),
    ("OG", "ONGOING"),
    ("ED", "ENDED")
]


# validacion nivel
def validateLevel(value):
    if (value < 1):
        raise ValidationError(
            "%(value) must be greater than 0", params={"value": value})

# Create your models here.


class User(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, null=False, blank=False)
    nickname = models.CharField(max_length=150, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)
    novice = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(
        max_length=12, blank=False, null=False, default=123456)
    characters = models.ForeignKey('Characters', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} {self.name} {self.email} {self.nickname} {self.is_admin}"


class Dm(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, null=False, blank=False)
    dmParty = models.ManyToManyField('Party')
    userId = models.OneToOneField('User', on_delete=models.CASCADE, blank=True, null=True)

class Party(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, null=False, blank=False)
    partySystem = models.CharField(max_length=150,choices=partyChoices, blank=False, null=False)
    partyState = models.CharField(max_length=150,choices=partyStatus, blank=False, null=False)
    partyIntro = models.TextField(blank=False, null=False)
    partyRules = models.TextField(blank=False, null=False)
    members = models.ForeignKey("User", on_delete=models.CASCADE)


class Characters(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=150, blank=False, null=False)
    nickname = models.CharField(max_length=150)
    characterClass = models.CharField(max_length=150, blank=False, null=False)
    level = models.IntegerField(validators=[validateLevel])
    modifiers = models.JSONField(null=False, blank=False)
    reputation = models.CharField(max_length=100, blank=True, null=True)
    relationships = models.CharField(max_length=100, blank=True, null=True)
    archetype = models.CharField(max_length=100, blank=True, null=True)
    healthPoints = models.IntegerField(blank=False, null=False, default=1)
    image = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return f"{self.name}{self.nickname} {self.id} {self.level} {self.modifiers}" 
