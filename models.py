from datetime import datetime

from sqlalchemy import create_engine, desc ,ForeignKey , MetaData,Text
from sqlalchemy import (CheckConstraint, UniqueConstraint,
    Column, DateTime, Integer, String ,Float)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'students'
    __table_args__ = (
        UniqueConstraint('email',
            name='unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12')
    )

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
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    comment = Column(Text)
    Vehicle_id = Column(Integer, ForeignKey('restaurants.id'))
    Customer_id = Column(Integer, ForeignKey('customers.id'))    
    vehicle = relationship('Restaurant', backref='reviews')
    customer = relationship('Customer', backref='reviews')