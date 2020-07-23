from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Thing, Sensor, Reading, TypeOfThing
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,timedelta,time


def thing_list(request):
	types = TypeOfThing.objects.all().order_by('name').annotate(things_count=Count('thing'))
	things_without_type = Thing.objects.filter(type_of_thing__isnull=True)
	return render(request, 'iotmonitor/thing_list.html',
				  {'types': types, 'things_without_type': things_without_type})


def thing_detail(request, pk):
	thing = Thing.objects.get(pk=pk)
	sensors = thing.sensor_set.all().order_by('name')
	return render(request, 'iotmonitor/thing_detail.html',
				  {'thing': thing, 'sensors': sensors})

#use the csrf_exempt tag since this view will be accessed from a external device
@csrf_exempt
def new_reading(request):
		user = authenticate(username=request.POST.get('device'), password=request.POST.get('password'))
		if user is not None:
			try:
				new_reading = Sensor.objects.get(pk=request.POST.get('id'))  # pk = sensor ID
				new_reading.reading_set.create(value=float(request.POST.get('value')))
				new_reading.save()
				return HttpResponse('device authenticated and data recorded')
			except:
				return HttpResponse('device authenticated but unable to record data')
		else:
			return HttpResponse('device not authenticated')