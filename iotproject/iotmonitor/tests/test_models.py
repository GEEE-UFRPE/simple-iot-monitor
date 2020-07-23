from django.test import TestCase

from ..models import TypeOfThing, Thing, Sensor, Reading
from django.utils import timezone



class ThingModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        TypeOfThing.objects.create(name='my type')

    def test_to_string(self):
        type_of_thing = TypeOfThing.objects.get(id=1)
        thing = Thing.objects.create(name='my thing', type_of_thing=type_of_thing)
        self.assertEqual(str(thing), 'my type my thing')

    def test_default_created_date_is_now(self):
        thing = Thing.objects.create()
        self.assertEqual(thing.created_date, timezone.now())

    # def test_description_is_mandatory(self):
    #     type_of_thing = TypeOfThing.objects.get(id=1)
    #     thing = Thing.objects.create(name='my thing', type_of_thing=type_of_thing)
    #     self.assertNotEqual(thing.description, '')
