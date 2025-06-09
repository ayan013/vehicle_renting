from models.vehicle import Vehicle
from models.car import Car
from models.bike import Bike
from models.client import Client
from services.RentLogic import RentLogic
from services.invoice import Invoice
from models.rent_details import Rent_Details

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
    print("3. Exit")
    choice = input("Enter your choice 1 or 2 or 3: ")
    try:
        if choice == "1":
            cars=rent_logic.show_cars()
            for car in cars:
                print(f"Id: {car.id} - {car.brand} - {car.rent} per day")
            car_choice = input("Tell me the ID of the car you want to rent:")
            days=int(input("For how many days: "))
            selected_car = None
            for car in cars:
                if car.id == car_choice:
                    selected_car = car
                    break

            name = input("Enter your Name: ")
            email = input("Enter your email")
            contact = int(input("Enter your mobile number: "))
            client = Client(name,email,contact)
            rental = Rent_Details(client=client,vehicle=selected_car,car=selected_car,bike=None,rent_logic=rent_logic)
            invoice=Invoice(rental,days)
            print(invoice.generate_invoice())
        elif choice == "2":
            bikes = rent_logic.show_bikes()
            for bike in bikes:
                print(f"Id: {bike.id} - {bike.brand} - {bike.rent} per day")
            bike_choice = input("Tell me the ID of the bike you want to rent:")
            days = int(input("For how many days:"))
            selected_bike=None
            for bike in bikes:
                if bike.id == bike_choice:
                    selected_bike = bike
                    break

            name = input("Enter your Name: ")
            email = input("Enter your email")
            contact = int(input("Enter your mobile number: "))
            client = Client(name, email, contact)
            rental = Rent_Details(client=client, vehicle=selected_bike, car=None , bike=selected_bike,
                                  rent_logic=rent_logic)
            invoice = Invoice(rental, days)
            print(invoice.generate_invoice())
        else:
            print("Exiting")
            break

    except ValueError as e:
        print("Wrong Choice")



