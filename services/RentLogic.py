from models.vehicle import Vehicle


class RentLogic:
    def __init__(self,tax:float,discount:int):
        self.cars=[]
        self.bikes=[]
        self.tax = tax
        self.discount = discount


    def add_car(self,car):
        return self.cars.append(car)

    def add_bike(self,bike):
        return self.bikes.append(bike)

    def total_cost(self,vehicle: Vehicle,days: int) -> float:
        subtotal = vehicle.calculate_cost(days)
        adding_tax = subtotal * (100 * self.tax)
        final_cost = adding_tax - self.discount
        return final_cost





