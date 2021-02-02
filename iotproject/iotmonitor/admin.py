from django.contrib import admin
from .models import Thing, Sensor, Reading, TypeOfThing
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class TypeOfThingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'description')

class ThingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'type_of_thing', 'description')
    list_filter = ['type_of_thing__name']
    search_fields = ['name']

class ReadingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('value', 'sensor_name', 'created_date')
    list_filter = ['sensor_name__name', 'created_date']
    search_fields = ['sensor_name__name']


admin.site.register(Reading, ReadingAdmin)
admin.site.register(TypeOfThing, TypeOfThingAdmin)
admin.site.register(Thing, ThingAdmin)

# Customize the User admin to add the Sensor data along with the authentication (User) data

class SensorInline(admin.StackedInline):
    model = Sensor
    can_delete = False
    verbose_name_plural = 'sensor'

class UserAdmin(BaseUserAdmin):
    inlines = (SensorInline,)
    list_display = ('username', 'sensor')
    list_filter = ['sensor__thing_monitored__name']
    search_fields = ['username', 'sensor__name', 'sensor__thing_monitored__name']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)