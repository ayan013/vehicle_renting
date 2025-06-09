from dataclasses import dataclass, field
from models.client import Client
from models.vehicle import Vehicle
from models.car import Car
from models.bike import Bike
from services.RentLogic import RentLogic

@dataclass
class Rent_Details:
    client:Client
    vehicle:Vehicle = field(default=None, init=False)
    car:Car = None
    bike:Bike = None
    days: int = 1
    rent_logic:RentLogic = None

    def __post_init__(self):
        if self.car:
            self.vehicle = self.car
        elif self.bike:
            self.vehicle = self.bike
        else:
            raise ValueError("Either car or bike must be provided to Rent_Details.")

