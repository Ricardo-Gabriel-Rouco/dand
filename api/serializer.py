from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Characters, Dm, Party, Desires, Relations


class ModifiersJsonField(serializers.JSONField):
    def to_internal_value(self, data):
        # Llamamos al método padre para obtener el valor interno
        value = super().to_internal_value(data)

        # Validamos que el JSON cumpla con el esquema
        allowed_keys = {"strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"}
        
        if not isinstance(value, dict):
            raise ValidationError("El campo debe ser un objeto JSON.")
        
        # Verificamos que no haya claves adicionales
        extra_keys = set(value.keys()) - allowed_keys
        if extra_keys:
            raise ValidationError(f"Se encontraron claves no permitidas: {', '.join(extra_keys)}")

        # Validamos que las claves permitidas sean enteros si están presentes
        for key in allowed_keys:
            if key in value and not isinstance(value[key], int):
                raise ValidationError(f"El valor de '{key}' debe ser un entero.")

        return value
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    modifiers = ModifiersJsonField()
    class Meta:
        model = Characters
        fields = '__all__'


class DmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dm
        fields = '__all__'


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class DesireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desires
        fields = '__all__'

class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relations
        fields = '__all__'