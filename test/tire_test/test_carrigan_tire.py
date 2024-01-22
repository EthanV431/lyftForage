import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_should_be_serviced(self):
        current_wear = [1, 0.5, 0.2, 0]
        tire = CarriganTire(current_wear)
        self.assertTrue(tire.needs_service())
    
    def test_should_not_be_serviced(self):
        current_wear = [0.32, 0.43, 0.6, 0.7]
        tire = CarriganTire(current_wear)
        self.assertFalse(tire.needs_service())