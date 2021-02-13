from django import template
from django.db.models import Max,Min,Avg
from django.utils import timezone


register = template.Library()

@register.filter
def max_value(list):
    maxvl = list.aggregate(Max('value'))
    return maxvl['value__max']

@register.filter
def min_value(list):
    minvl = list.aggregate(Min('value'))
    return minvl['value__min']

@register.filter
def avg_value(list):
    avgvl = list.aggregate(Avg('value'))
    return avgvl['value__avg']

@register.filter
def is_today(list):
    return list.filter(created_date__date=timezone.now().astimezone().date())

