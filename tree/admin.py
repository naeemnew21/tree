from django.contrib import admin
from .models import Person, Family, Hist, Log_Info

admin.site.register(Person)
admin.site.register(Family)
admin.site.register(Hist)
admin.site.register(Log_Info)