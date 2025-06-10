from models.car import Car
from models.bike import Bike
from services.RentLogic import RentLogic
from repositories.Inventory import Inventory
from cli.cli import rent_vehicle

rent_logic=RentLogic(0.20,100)
inventory=Inventory()

inventory.add_car(Car(101,"car",500,True,"Maruti Wagon R","Petrol",5))
inventory.add_car(Car(102,"car",700,True,"Hyundai i10","Petrol",5))
inventory.add_car(Car(103,"car",1000,False,"Maruti Ertiga","Diesel",7))
inventory.add_car(Car(104,"car",1200,True,"Innova","Petrol",8))

inventory.add_bike(Bike(201,"bike",200,True,"Super Splendor",120,60))
inventory.add_bike(Bike(202,"bike",300,False,"Pulser",140,50))
inventory.add_bike(Bike(203,"bike",400,True,"KTM",220,45))
inventory.add_bike(Bike(204,"bike",500,True,"Royal Enfield",350,35))

while True:
    print("----Menu----")
    print("1. Rent a Car")
    print("2. Rent a Bike")
    print("3. Exit")
    choice = input("Enter your choice 1 or 2 or 3: ")
    try:
        if choice == "1":
            rent_vehicle("car",inventory,rent_logic)
        elif choice == "2":
            rent_vehicle("bike",inventory,rent_logic)
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("You have entered wrong value")

    except ValueError as e:
        print(e)



