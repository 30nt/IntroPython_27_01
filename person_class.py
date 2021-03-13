class Person:
    def __init__(self, name="Anna", age=12):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def __repr__(self):
        return f"({self.name}, {self.age})"

    def increase_age(self, years_number=1):
        self.age += years_number


john = Person("John", 23)
jack = Person("Jack", 43)
noname = Person()

print(noname, jack,  [jack, john])
# print(john.name, john.age)
# john.increase_age()
# john.increase_age()
# print(john.name, john.age)
# jack.increase_age(10)
# print(jack.age)
