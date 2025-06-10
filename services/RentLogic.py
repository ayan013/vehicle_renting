from models.vehicle import Vehicle

class RentLogic:
    def __init__(self,tax:float,discount:int):
        self.tax = tax
        self.discount = discount

    def total_cost(self,vehicle: Vehicle,days: int) -> float:
        subtotal = vehicle.calculate_cost(days)
        adding_tax = subtotal + (subtotal * self.tax)
        final_cost = adding_tax - self.discount
        return final_cost





