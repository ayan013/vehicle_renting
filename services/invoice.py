from datetime import datetime
from uuid import uuid4
from models.rent_details import Rent_Details
from models.car import Car
from models.bike import Bike


class Invoice:
    def __init__(self, rental:Rent_Details,days:int):
        self.rental = rental
        self.days= days
        self.invoice_id = uuid4()
        self.date = datetime.now()
        self.tax=self.rental.vehicle.calculate_cost(days) * self.rental.rent_logic.tax


    def generate_invoice(self):
         base_info= f"""
         ------------------Rental Invoice-------------------
         ID : {self.invoice_id}
         Date: {self.date}
         
         Name: {self.rental.client.name}
         Email: {self.rental.client.email}
         Contact: {self.rental.client.contact}
         ---------------------------------------------------
         Vehicle Type: {self.rental.vehicle.type}
         """
         if isinstance(self.rental.vehicle, Car):
             vehicle_info = f"""
              Brand: {self.rental.car.brand}
              Fuel: {self.rental.car.fuel_type}
              Seating Capacity: {self.rental.car.seater}             
              """
         elif isinstance(self.rental.vehicle, Bike):
              vehicle_info=f"""
              Brand: {self.rental.bike.brand} - {self.rental.bike.cc}
              Mileage: {self.rental.bike.mileage}
              """
         else:
             vehicle_info = "\n No vehicle-specific details found.\n"
         total_cost=f"""
         Rent: {self.rental.vehicle.rent}
         Days: {self.days}
         ----------------------------------------------------
         Sub Total: {self.rental.vehicle.calculate_cost(self.days)}
         Tax (+): {self.tax}
         Discount (-): {self.rental.rent_logic.discount}
         ----------------------------------------------------
         Total Cost: {self.rental.rent_logic.total_cost(self.rental.vehicle,self.days) }
         """
         return base_info + vehicle_info + total_cost
         
         

