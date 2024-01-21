from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

class Engine(ABC):
    def __init__(self, last_service_mileage, current_mileage, warning_light_on):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.warning_light_on = warning_light_on

class Car(ABC):
    def __init__(self, current_date = datetime.today().date(), last_service_date = datetime.today().date(), last_service_mileage = 0, current_mileage = 0, warning_light_on = False):
        self.battery = Battery(current_date, last_service_date)
        self.engine = Engine(last_service_mileage, current_mileage, warning_light_on)

    @abstractmethod
    def needs_service(self):
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        else:
            return False
