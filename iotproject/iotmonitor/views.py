from django.db.models import Count
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Thing, TypeOfThing
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


def thing_list(request):
	types = TypeOfThing.objects.all().order_by('name').annotate(things_count=Count('thing'))
	things_without_type = Thing.objects.filter(type_of_thing__isnull=True)
	return render(request, 'iotmonitor/thing_list.html',
				  {'types': types, 'things_without_type': things_without_type})


def thing_detail(request, pk):
	thing = Thing.objects.get(pk=pk)
	sensors = thing.sensor_set.all().order_by('name')
	return render(request, 'iotmonitor/thing_detail.html',
				  {'thing': thing, 'sensors': sensors,})

#use the csrf_exempt tag since this view will be accessed from a external device
@csrf_exempt
@require_POST
def new_reading(request):
	#use POST parameters to authenticate
	user = authenticate(username=request.POST.get('sensor'), password=request.POST.get('password'))
	if user is not None:
		try:
			user.sensor.reading_set.create(value=float(request.POST.get('value')))
			user.sensor.save()
			return HttpResponse('Sensor authenticated and data succesfully recorded.')

		except:
			return HttpResponseBadRequest('Sensor authenticated but unable to record data. Make sure your sensor provided a value that can be parsed onto a numerical value.')
	else:
		response = HttpResponse('Sensor not authenticated. Please check its username ({}) and password.'.format(request.POST.get('sensor')), status=401)
		return response
