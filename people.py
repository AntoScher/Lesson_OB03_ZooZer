# people.py

class People:
    def __init__(self, name):
        self.name = name

    def activity(self):
        raise NotImplementedError("This method should be overridden in subclasses")

# Подклассы
class Visitor(People):
    def activity(self):
        return f"{self.name} is watching animals."

class Employee(People):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def activity(self):
        return f"{self.name} is taking care of animals."

class Manager(People):
    def activity(self):
        return f"{self.name} is managing the zoo."

class ZooKeeper(Employee):
    def feed_animal(self):
        return f"{self.name} is feeding the animals."

class Veterinarian(Employee):
    def heal_animal(self):
        return f"{self.name} is healing the animals."
