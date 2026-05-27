from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer, Car, Driver


class CarSearchTests(TestCase):
    def test_search_by_model(self):
        manufacturer = Manufacturer.objects.create(name="BMW")
        Car.objects.create(model="X5", manufacturer=manufacturer)
        Car.objects.create(model="X3", manufacturer=manufacturer)
        response = self.client.get(reverse("car-list"), {"model": "X5"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["cars"]), 1)


class DriverSearchTests(TestCase):
    def test_search_by_username(self):
        Driver.objects.create(username="john")
        Driver.objects.create(username="mike")
        response = self.client.get(reverse("driver-list"), {"username": "john"})
        self.assertEqual(len(response.context["drivers"]), 1)


class ManufacturerSearchTests(TestCase):
    def test_search_by_name(self):
        Manufacturer.objects.create(name="Tesla")
        Manufacturer.objects.create(name="Toyota")
        response = self.client.get(reverse("manufacturer-list"), {"name": "Tesla"})
        self.assertEqual(len(response.context["manufacturers"]), 1)