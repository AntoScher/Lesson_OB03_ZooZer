# animal.py

class Animal:
    def __init__(self, alias, age):
        self.alias = alias
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def eat(self):
        return f"{self.alias} is eating."

# Подклассы
class Bird(Animal):
    def __init__(self, alias, age, wing_span):
        super().__init__(alias, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Tweet tweet"

    def motion(self):
        return "Flying"

class Mammal(Animal):
    def __init__(self, alias, age, fur_type):
        super().__init__(alias, age)
        self.fur_type = fur_type

    def make_sound(self):
        return "Roar"

    def motion(self):
        return "Running"

# Агрегация
class Predator(Mammal):
    def __init__(self, alias, age, fur_type, fangs):
        super().__init__(alias, age, fur_type)
        self.fangs = fangs

    def attack(self):
        return f"{self.alias} is attacking with its fangs!"

class Herbivorous(Mammal):
    def __init__(self, alias, age, fur_type, horns):
        super().__init__(alias, age, fur_type)
        self.horns = horns

    def flee(self):
        return f"{self.alias} is fleeing with its horns!"

class Reptile(Animal):
    def __init__(self, alias, age, skin_type):
        super().__init__(alias, age)
        self.skin_type = skin_type

    def make_sound(self):
        return "Hiss"

    def motion(self):
        return "Crawling"
