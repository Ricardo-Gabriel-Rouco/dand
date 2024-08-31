from django.contrib import admin
from .models import UserProfile, Party, Dm, Characters

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Party)
admin.site.register(Dm)
admin.site.register(Characters)