from django.db import models
from django.utils import timezone
#AO ALTERAR O ARQUIVO NÃO ESQUECER:
#python manage.py makemigrations
#python manage.py migrate

class TypeOfThing(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField(max_length=200)
    type_of_thing = models.ForeignKey(TypeOfThing, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    thing_monitored = models.ForeignKey(Thing, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

class Reading(models.Model):
    sensor_name = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.value)