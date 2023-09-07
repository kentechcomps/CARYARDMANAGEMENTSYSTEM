from datetime import datetime
from sqlalchemy import create_engine, desc ,ForeignKey , MetaData,Text
from sqlalchemy import (CheckConstraint, UniqueConstraint,
    Column, DateTime, Integer, String ,Float)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///Caryard.db')
Session=sessionmaker(bind=engine)
session=Session()

class Vehicle(Base):
    __tablename__ = 'Vehicles'

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    is_sold = Column(Integer, default=0)
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"
    
class Customer(Base):
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

class Review(Base):
    __tablename__ = 'Reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    comment = Column(Text)
    Vehicle_id = Column(Integer, ForeignKey('Vehicles.id'))
    Customer_id = Column(Integer, ForeignKey('Customers.id'))    
    vehicle = relationship('Vehicle', backref='Reviews')
    customer = relationship('Customer', backref='Reviews')