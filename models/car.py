from models.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,id: int, type: str, rent: int, is_available: bool, brand:str, fuel_type: str, seater:int):
        super().__init__(id, type, rent, is_available)
        self.brand = brand
        self.fuel_type = fuel_type
        self.seater = seater

    def __str__(self):
        return f"Brand: {self.brand}\n Fuel - {self.fuel_type}\n Ideal for {self.seater} people\n"

