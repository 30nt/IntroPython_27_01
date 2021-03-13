# Класс
# Экземпляр класса
# Атрибут класса   - используем для конкретной задачи
# Атрибут экземпляра класса - используем почти всегда
# Метод класса  - функция класса используем для конкретной задачи
# Метод экземпляра класса - функция используем почти всегда

class Person:  # Класс
    # pass
    name = "Anna"  # Атрибут класса
    age = 0  # Атрибут класса

person_1 = Person()  # Экземпляр класса
person_2 = Person()  # Экземпляр класса
# print(">>>>", person_1.name, person_2.name)

person_1.name = "John" # Атрибут экземпляра класса
person_2.name = "Jack"
person_1.sex = "male"

print(person_1.name, person_2.name, person_1.sex, person_2)

# Person.name = "Denis"
# print(">>>>", person_1.name, person_2.name)
# person_3 = Person()
# print(person_3.name)


# person_1_test = person_1
# print(person_1.name, person_2.name, person_1 is person_2, person_1 is person_1_test)