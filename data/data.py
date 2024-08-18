# Создадим класс с параметрами человека @dataclass
#Протишем строковый тип данных в дата-классе
from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
