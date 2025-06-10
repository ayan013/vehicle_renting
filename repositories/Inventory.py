

class Inventory:
    def __init__(self):
        self.cars = []
        self.bikes = []

    def add_car(self,car):
        return self.cars.append(car)

    def add_bike(self,bike):
        return self.bikes.append(bike)

    def show_cars(self):
        return self.cars

    def show_bikes(self):
        return self.bikes

    def get_car_by_id(self,car_id):
        for car in self.cars:
            if car.id == car_id:
                return car
        return None

