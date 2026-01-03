class BMW:
    def start_engine(self):
        print("BMW engine roars to life! Vroom vroom!")
class Ferrari:
    def start_engine(self):
        print("Ferrari engine ignites with a roar! Brum brum!")
def car_start(car):
    print(car.start_engine())
bmw_car = BMW()
ferrari_car = Ferrari()
car_start(bmw_car)
car_start(ferrari_car)