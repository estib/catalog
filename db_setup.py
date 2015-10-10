__author__ = 'Steve'

# this file creates the database that is used for the catalog app.
# in order for it to work, you must first go into PSQL and create a database
# called "catalog_db".

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    creator_id = Column(String, nullable=False)
    item_rel = relationship("Items", cascade="save-update, merge, delete")


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer,
                         ForeignKey('category.id'),
                         nullable=False
                         )
    creator_id = Column(String, nullable=False)
    pic_url = Column(String, nullable=True)
    category_rel = relationship(Category)


engine = create_engine('postgresql+psycopg2:///catalog_db')

Base.metadata.create_all(engine)
