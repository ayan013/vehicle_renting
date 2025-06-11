from db_models.car_model import CarModel

#  DB operations - CRUD
def add_car(session,car:CarModel):
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

def get_car_by_id(session,car_id: int):
    car=session.query(CarModel).filter_by(id=car_id).first()
    return car

def get_all_car(session):
    cars=session.query(CarModel).filter_by(is_available=True).all()
    return cars

def mark_car_unavailable(session, car_id: int):
    car=get_car_by_id(session,car_id)
    if car:
        car.is_available = False
        session.commit()




