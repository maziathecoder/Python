class vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class bus(vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge
bus = bus(50)
print("total bus fare: INR", bus.fare())
