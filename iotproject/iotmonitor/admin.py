from django.contrib import admin
from .models import Thing, Sensor, Reading, TypeOfThing

class TypeOfThingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'description')

class ThingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'type_of_thing', 'description')
    list_filter = ['type_of_thing__name']
    search_fields = ['name']

class SensorAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'thing_monitored', 'description')
    list_filter = ['thing_monitored__name']
    search_fields = ['name', 'thing_monitored__name']

class ReadingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('value', 'sensor_name', 'created_date')
    list_filter = ['sensor_name__name', 'created_date']
    search_fields = ['sensor_name__name']

admin.site.register(Reading, ReadingAdmin)
admin.site.register(TypeOfThing, TypeOfThingAdmin)
admin.site.register(Thing, ThingAdmin)
admin.site.register(Sensor, SensorAdmin)
