from models.vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, id: int, type: str, rent: int, is_available: bool, brand:str, cc:int, mileage:int):
        super().__init__(id, type, rent, is_available)
        self.brand = brand
        self.cc = cc
        self.mileage = mileage

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}\nBrand : {self.brand}\n CC : {self.cc}\n Mileage(Aprrox): {self.mileage}"
