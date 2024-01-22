from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, current_wear):
        self.current_wear = current_wear
    
    def needs_service(self):
        for i in self.current_wear:
            if i >= 0.9:
                return True
        return False