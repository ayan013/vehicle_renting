from sqlalchemy import Integer, String, Boolean, Column
from db.database import Base

# SQLAlchemy Car table
class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer,primary_key=True,index=True)
    type = Column(String,default="car")
    rent = Column(Integer)
    is_available = Column(Boolean,default=True)
    brand = Column(String)
    fuel_type = Column(String)
    seater = Column(Integer,default=4)