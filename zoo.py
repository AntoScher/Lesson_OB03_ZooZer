# zoo.py

from animal import Bird, Mammal, Reptile, Predator, Herbivorous
from people import Visitor, Employee, Manager, ZooKeeper, Veterinarian

class Zoo:
    def __init__(self):
        self.animals = []
        self.people = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_person(self, person):
        self.people.append(person)

    def save_zoo(self, filename):
        with open(filename, 'w') as file:
            file.write("Animals:\n")
            for animal in self.animals:
                file.write(f"{animal.alias}, {animal.age}\n")
            file.write("\nPeople:\n")
            for person in self.people:
                file.write(f"{person.name}\n")

    def load_zoo(self, filename):
        with open(filename, 'r') as file:
            content = file.readlines()
            for line in content:
                print(line.strip())

    def display_zoo(self):
        print("Animals in the Zoo:")
        for animal in self.animals:
            print(f"{animal.alias}, {animal.age}")
        print("\nPeople in the Zoo:")
        for person in self.people:
            print(f"{person.name}")
