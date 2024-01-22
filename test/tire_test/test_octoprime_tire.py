import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_should_be_serviced(self):
        current_wear = [1, 1, 1, 0]
        tire = OctoprimeTire(current_wear)
        self.assertTrue(tire.needs_service())
    
    def test_should_not_be_serviced(self):
        current_wear = [0.32, 0.43, 0.6, 0.7]
        tire = OctoprimeTire(current_wear)
        self.assertFalse(tire.needs_service())