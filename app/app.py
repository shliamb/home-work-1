import time
#from psycopg2 import OperationalError
#import psycopg2
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import sessionmaker
from models import Base, Menu, Submenu, Dish
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine

engine = create_engine('postgresql://admin:12345@localhost:5432/my_database')
Session = sessionmaker(bind=engine)
#Base.metadata.create_all(engine)


app = FastAPI()

#time.sleep(10)

# Здесь добавь эндпойнты для CRUD-операций

if __name__ == "__main__":
    Base.metadata.create_all(engine)












# Скрипт в постмане который возможо поможет

# скрипт в тесте  
# // check that response status HTTP 201 CREATED 
# pm.test("Status code is 201", () => { 
#   pm.response.to.have.status(201); 
# }); 
 
# // Save env vars 
# postman.setEnvironmentVariable('target_menu_id', responseJSON.id); 
# postman.setEnvironmentVariable('target_menu_title', responseJSON.title); 
# postman.setEnvironmentVariable('target_menu_description', responseJSON.description); 
 
# // check that 'target_menu_id' from environment & response are equal 
# pm.test("Response contains 'id' property", () => { 
#   pm.expect(pm.environment.get('target_menu_id')).to.eql(responseJSON.id); 
# }); 
 
# // check that 'target_menu_title' from environment & response are equal 
# pm.test("Response contains 'title' property", () => { 
#   pm.expect(pm.environment.get('target_menu_title')).to.eql(responseJSON.title); 
# }); 
 
# // check that 'target_menu_description' from environment & response are equal 
# pm.test("Response contains 'description' property", () => { 
#   pm.expect(pm.environment.get('target_menu_description')).to.eql(responseJSON.description); 
# });