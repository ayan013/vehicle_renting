from sqlalchemy import Integer, String, Column, Boolean
from db.database import Base

class BikeModel(Base):
    __tablename__ = "bikes"

    id = Column(Integer,primary_key=True,index=True)
    type = Column(String,default="bike")
    rent = Column(Integer)
    is_available = Column(Boolean,default=True)
    brand = Column(String)
    cc = Column(Integer)
    mileage = Column(Integer)