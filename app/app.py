from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import sessionmaker, Session
from .models import Base, Menu, Submenu, Dish
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from .schemas import MenuCreate, BaseModel, MenuResponse
from typing import List

engine = create_engine('postgresql://admin:12345@localhost:5432/my_database')
Session = sessionmaker(bind=engine)

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Эндпойнты для CRUD-операций
# Добавление меню
@app.post("/api/v1/menus/", response_model=MenuResponse, status_code=status.HTTP_201_CREATED)
def create_menu(menu_data: MenuCreate, db: Session = Depends(get_db)):
    new_menu = Menu(title=menu_data.title, description=menu_data.description)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return MenuResponse(id=new_menu.id, title=new_menu.title, description=new_menu.description)

# получение списка меню или конкретного меню по ID
@app.get("/api/v1/menus/", response_model=List[MenuResponse])
def read_menus(db: Session = Depends(get_db)):
    menus = db.query(Menu).all()
    return menus

# @app.get("/menus/{menu_id}")
# def read_menu(menu_id: int, db: Session = Depends(get_db)):
#     return db.query(Menu).filter(Menu.id == menu_id).first()

# # Обновление информации о меню
# @app.put("/menus/{menu_id}")
# def update_menu(menu_id: int, name: str = Body(..., embed=True), db: Session = Depends(get_db)):
#     db.query(Menu).filter(Menu.id == menu_id).update({"name": name})
#     db.commit()
#     return db.query(Menu).filter(Menu.id == menu_id).first()

# # Dellete
# @app.delete("/menus/{menu_id}")
# def delete_menu(menu_id: int, db: Session = Depends(get_db)):
#     db.query(Menu).filter(Menu.id == menu_id).delete()
#     db.commit()
#     return {"message": "Menu deleted"}

# @app.get("/menus/{menu_id}")
# def read_menu(menu_id: int, db: Session = Depends(get_db)):
#     menu = db.query(Menu).filter(Menu.id == menu_id).first()
#     if menu is None:
#         raise HTTPException(status_code=404, detail="Menu not found")
#     return menu

if __name__ == "__main__":
    Base.metadata.create_all(engine)









# Цены блюд выводить с округлением до 2 знаков после запятой:
# Нет, не соответствует. Это должно быть реализовано в логике запроса или в
# представлении, а не на уровне модели данных.
    
# Во время выдачи списка меню добавлять количество подменю и блюд:
# Нет, не соответствует. Для этого нужно реализовать дополнительную логику в запросах к базе данных.

# Во время выдачи списка подменю добавлять количество блюд:
# Нет, не соответствует. Аналогично предыдущему пункту, требуется дополнительная логика в запросах.

# БД должна быть пуста при запуске тестов:
# Не соответствует. Для этого нужно добавить логику очистки базы данных перед запуском тестов.
    

# Однако, для полного соответствия заданию на разработку REST API на FastAPI с использованием PostgreSQL, вам нужно учитывать следующее:

# CRUD операции: Вам нужно реализовать эндпоинты API для создания, чтения, обновления и удаления (CRUD) для каждой из этих сущностей. Это включает в себя маршруты для обработки HTTP-запросов, таких как GET, POST, PUT и DELETE.

# Валидация данных: Реализация валидации входящих данных для этих операций.

# Интеграция с базой данных: Настройка и подключение к PostgreSQL, а также операции с базой данных для каждого действия CRUD.

# Тестирование: Для проверки задания у вас должны быть тесты, возможно, с использованием Postman, чтобы убедиться, что API работает корректно.

# Дополнительная логика: Реализация логики для специфических условий, например, подсчет количества подменю и блюд в каждом меню, округление цен до 2 знаков после запятой и т.д.



# # Создание сессии
# session = Session()

# Session.execute(text("SELECT 1"))
# print("Соединение с базой данных установлено успешно.")
# session.close()


# Папка "Проверка кол-ва блюд и подменю в меню", "Просматривает список блюд"
# GET {{LOCAL_URL}}/api/v1/menus/{{target_menu_id}}/submenus/{{target_submenu_id}}/dishes
# Для удаленного подменю тест ожидает 200, [].
# По идее, запрос должен возвращать 
# 404
# {
#     "detail": "submenu not found"
# }


# В папке "CRUD для меню" последний тест для несуществующего меню ожидает же 404 "menu not found", поэтому 
# GET {{LOCAL_URL}}/api/v1/menus/{{target_menu_id}}/submenus/{{target_submenu_id}}/dishes тоже должен ожидать 404 "submenu not found"

    




# {
#     "id": "9a5bce5f-4462-4d12-a66c-d59584b19ee8",
#     "title": "My menu 1",
#     "description": "My menu description 1",
#     "submenus_count": 0,
#     "dishes_count": 0
# }



# подсказка Pydantic. Он гарантирует, что значение, переданное в поле uuid, соответствует формату UUID4
    

# default=uuid.uuid4