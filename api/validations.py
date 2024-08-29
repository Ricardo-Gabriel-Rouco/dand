from django.core.exceptions import ValidationError

# validacion nivel
def validateLevel(value):
    if (value < 1):
        raise ValidationError(
            "%(value) must be greater than 0", params={"value": value})

# validacion armor class
def validateArmorClass(value):
    if (value < 1):
        raise ValidationError(
            "%(value) must be greater than 0", params={"value": value})
    try:
        value = int(value)
    except:
        raise ValidationError("%(value) must be a number", params={"value": value})