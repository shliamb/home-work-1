# Классы SQLAlchemy для таблиц базы данных
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

# Menu
class Menu(Base):
    __tablename__ = 'menu'
    # id = Column(Integer, primary_key=True) # "id": "9a5bce5f-4462-4d12-a66c-d59584b19ee8",
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False) 
    title = Column(String(50))
    description = Column(String(50))
    submenus = relationship("Submenu", cascade="all, delete")

# Submenu
class Submenu(Base):
    __tablename__ = 'submenu'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    menu_id = Column(UUID(as_uuid=True), ForeignKey('menu.id'))
    name = Column(String)
    dishes = relationship("Dish", cascade="all, delete")

# dish
class Dish(Base):
    __tablename__ = 'dish'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey('submenu.id'))
    name = Column(String)
    price = Column(Float)

engine = create_engine('postgresql://admin:12345@localhost:5432/my_database')
Base.metadata.create_all(engine)