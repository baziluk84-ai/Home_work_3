import json
from typing import List
from pydantic import BaseModel


class SystemUser(BaseModel):
    id: int
    username: str
    email: str
    password: str
    surname: str
    name: str
    is_active: bool
    address: dict
    contacts: list

#Об’єкт класу SystemUser

user = SystemUser(id = 12345, username = "admin",
                  email = "admin@gmail.com", password = "753159", surname = "Rembo", name= "John",
                  is_active = True, address = {'city': 'Kyev', 'street': '123 Main Street'}, contacts=["phone: 0671775566", "work_phone: 0441246424", "fax: 0441223333"])


print(user)

#Перетворюємо зміну у JSON-рядок
system_user = user.model_dump_json()
#print(system_user)

#Записуємо у JSON-файл
with open('system_user.json', 'w') as f:
    f.write(system_user)


#Читаємо файл
with open('system_user.json', 'r') as f:
    #Перетворюємо вміст назад у об’єкт
    system_user = json.load(f)
    print(f"User configuration:",  system_user)