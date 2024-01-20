# Pydantic-модели, которые определяют структуру входных и выходных данных твоего API

from pydantic import BaseModel, UUID4
from typing import Optional

# Это схема для создания нового объекта "меню"
class MenuCreate(BaseModel):
    #id: UUID4
    title: str
    description: str

# Эта схема может быть использована для ответа, возвращающего данные о меню
class MenuResponse(BaseModel):
    id: UUID4
    title: str
    description: str

# Если нужно обновить данные о меню, можно использовать эту схему
class MenuUpdate(BaseModel):
    #id: UUID4
    title: Optional[str] = None
    description: Optional[str] = None


# MenuCreate: используется, когда пользователь отправляет данные для создания нового меню.
# MenuResponse: используется для отправки данных об объекте меню клиенту.
# MenuUpdate: используется, когда данные меню обновляются.
# Таким образом, schemas.py отвечает за структуру данных (сериализацию), которые входят в твоё API и выходят из него. Это облегчает валидацию и сериализацию данных.