import unittest
from datetime import datetime

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        warning_light_is_on = True
        last_service_date = datetime.today().date()
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())
    
    def test_should_be_serviced(self):
        warning_light_is_on = False
        last_service_date = datetime.today().date()
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(engine.needs_service())