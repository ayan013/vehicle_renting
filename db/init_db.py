from db.database import engine,Base
from db.db_models.car_model import CarModel

#  Create tables (run once for everytime a new table created
#  it will change once data migration tool will be used eg: alembic)

def init_db():
    Base.metadata.create_all(bind=engine)