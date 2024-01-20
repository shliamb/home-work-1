from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()


# Menu
class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    submenus = relationship("Submenu", cascade="all, delete")

# Submenu
class Submenu(Base):
    __tablename__ = 'submenu'
    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, ForeignKey('menu.id'))
    name = Column(String)
    dishes = relationship("Dish", cascade="all, delete")

# dish
class Dish(Base):
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True)
    submenu_id = Column(Integer, ForeignKey('submenu.id'))
    name = Column(String)
    price = Column(Float)

