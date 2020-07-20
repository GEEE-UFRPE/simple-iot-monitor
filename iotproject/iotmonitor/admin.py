from django.contrib import admin
from .models import Thing, Sensor, Reading, TypeOfThing


admin.site.register(Thing)
admin.site.register(Sensor)
admin.site.register(Reading)
admin.site.register(TypeOfThing)
