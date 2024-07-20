from rest_framework import serializers

class statsSerializer(serializers.Serializer):
  strength = serializers.IntegerField(required=False)
  dexterity = serializers.IntegerField(required=False)
  constitution = serializers.IntegerField(required=False)
  wisdom = serializers.IntegerField(required=False)
  inteligence = serializers.IntegerField(required=False)
  charisma = serializers.IntegerField(required=False)