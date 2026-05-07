from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    count = Column(Integer, nullable=False)
    description = Column(String(500), nullable=False)

