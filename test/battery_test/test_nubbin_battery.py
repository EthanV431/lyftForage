import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 1)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())