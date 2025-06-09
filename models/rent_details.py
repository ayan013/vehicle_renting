from dataclasses import dataclass
from models.client import Client
from models.vehicle import Vehicle
from models.car import Car
from models.bike import Bike
from services.RentLogic import RentLogic

@dataclass
class Rent_Details:
    client:Client
    vehicle:Vehicle
    car:Car
    bike:Bike
    rent_logic:RentLogic

