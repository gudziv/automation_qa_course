# Создадим функцию генератора человека
# Функция generated_person() будет вызывать класс с полями
# для этого импортируем этот класс
# Установим библиотеку faker и импортируем из нее Faker
from data.data import Person
from faker import Faker


# Обозначим у faker русский язык
faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )