from models.vehicle import Vehicle
from models.car import Car
from models.bike import Bike
from services.RentLogic import RentLogic


rent_logic=RentLogic(0.20,1500)

rent_logic.add_car(Car(101,"car",500,True,"Maruti Wagon R","Petrol",5))
rent_logic.add_car(Car(102,"car",700,True,"Hyundai i10","Petrol",5))
rent_logic.add_car(Car(203,"car",1000,True,"Maruti Ertiga","Diesel",7))
rent_logic.add_car(Car(204,"car",1200,True,"Innova","Petrol",8))

rent_logic.add_bike(Bike(201,"bike",200,True,"Super Splendor",120,60))
rent_logic.add_bike(Bike(202,"bike",300,True,"Pulser",140,50))
rent_logic.add_bike(Bike(203,"bike",400,True,"KTM",220,45))
rent_logic.add_bike(Bike(204,"bike",500,True,"Royal Enfield",350,35))

while True:
    print("----Menu----")
    print("1. Rent a Car")
    print("2. Rent a Bike")
    choice = input(print("Enter your choice 1 or 2 : "))
    try:
        if choice == 1:
            cars=rent_logic.show_cars()
            for car in cars:
                print(f"Id: {car.id} - {car.brand} - {car.rent} per day")
            car_choice = input(print("Tell me the ID of the car you want to rent:"))
            days=input(print("For how many days:"))

    except:
        print("Wrong Choice")



