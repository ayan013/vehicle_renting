from models.client import Client
from models.rent_details import Rent_Details
from services.invoice import Invoice

def get_vehicle_list(vehicles):
    for vehicle in vehicles:
        if vehicle.is_available is True:
            print(f"Id: {vehicle.id} - {vehicle.brand} - {vehicle.rent} per day")
        else:
            continue

def select_vehicle(vehicles,vehicle_type):
    if vehicle_type == "car":
        vehicle_id = int(input("Enter the ID of the Car - "))
    else:
        vehicle_id = int(input("Enter the ID of the Bike - "))
    for vehicle in vehicles:
        if vehicle.id == vehicle_id:
            return vehicle
    return None

def client_info():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    contact = int(input("Enter your Mobile number: "))
    return Client(name,email,contact)


def rent_vehicle(vehicle_type,inventory, rent_logic):
    if vehicle_type == "car":
        vehicles = inventory.show_cars()
    else:
        vehicles = inventory.show_bikes()

    get_vehicle_list(vehicles)
    selected = select_vehicle(vehicles,vehicle_type)
    if not selected:
        return

    try:
        days = int(input("For how many day? "))
    except ValueError:
        print("Invalid input for days")
        return

    client=client_info()

    rental = Rent_Details(
        client=client,
        car=selected if vehicle_type == "car" else None,
        bike=selected if vehicle_type == "bike" else None,
        days=days,
        rent_logic=rent_logic)

    invoice = Invoice(rental,days)
    print(invoice.generate_invoice())
    selected.mark_rented()


