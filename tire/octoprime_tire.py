from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, current_wear):
        self.current_wear = current_wear
    
    def needs_service(self):
        total_wear = 0
        for i in self.current_wear:
            total_wear += i
        if total_wear >= 3:
            return True
        return False
