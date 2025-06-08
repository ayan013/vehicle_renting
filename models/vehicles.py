class Vehicles:
    def __init__(self, id: int, type: str, rent: int, is_available: str ):
        self.id = id
        self.type = type
        self.rent = rent
        self.is_available = is_available


class Car(Vehicles):
    def add_car(self,type_fuel:str,capacity:int,boot_space:int):
        return None

