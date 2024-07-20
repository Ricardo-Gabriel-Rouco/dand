from django.contrib import admin
from  .models import User, Party, Dm, Characters

# Register your models here.
admin.site.register(User)
admin.site.register(Party)
admin.site.register(Dm)
admin.site.register(Characters)