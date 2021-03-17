class Unit:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.intellect = 1
        self.agility = 1

    def __repr__(self):
        return f"name: {self.name}, " \
               f"intellect: {self.intellect}, " \
               f"agility: {self.agility}"

    def increase(self):
        raise NotImplementedError


class Mage(Unit):
    def __init__(self, name, armor):
        super().__init__(name)
        self.armor = armor

    def __repr__(self):
        return "Mage: " + super().__repr__()

    def increase(self):
        self.intellect += 1


class Archer(Unit):
    def increase(self):
        self.agility += 1


class Warrior(Unit):
    def increase(self):
        pass

    def __repr__(self):
        return "qwerty"



# aragorn = Warrior("Aragorn")
# aragorn.increase()
# print(aragorn)

gendalf = Mage("Gendalf", "staff")
print(gendalf)
gendalf.increase()
print(gendalf)
#
# legolass = Archer("Legolas")
# print(legolass)
# legolass.increase()
# print(legolass)


