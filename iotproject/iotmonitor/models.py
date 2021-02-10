from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# after changing the models, update the database with these commands
#   python manage.py makemigrations
#   python manage.py migrate
# and also remember to update the database_diagram.txt file in the root folder

class TypeOfThing(models.Model):
    name = models.CharField('Type of thing', max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField('Thing', max_length=200, unique=True)
    type_of_thing = models.ForeignKey(TypeOfThing, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        result = ''
        if self.type_of_thing:
            # if this thing is associated with a type, add the type to the string
            # this makes it easier to identify the thing when there are multiple types of things recorded
            result = '{} {}'.format(self.type_of_thing.name, self.name)
        else:
            result = self.name
        return result

class Sensor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Sensor name', max_length=200)
    thing_monitored = models.ForeignKey(Thing, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} - {}'.format(self.thing_monitored.__str__(), self.name)

class Reading(models.Model):
    sensor_name = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return str(self.value)