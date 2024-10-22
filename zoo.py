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


    def get_formatted_zoo_list(self):
        """Возвращает отформатированный список объектов зоопарка."""

        output = "## Содержание\n"
        output += "1. [Животные](#животные)\n"
        output += "   1. [Птицы](#птицы)\n"
        output += "   2. [Млекопитающие](#млекопитающие)\n"
        output += "      1. [Хищники](#хищники)\n"
        output += "      2. [Травоядные](#травоядные)\n"
        output += "   3. [Рептилии](#рептилии)\n"
        output += "2. [Люди](#люди)\n"
        output += "   1. [Посетители](#посетители)\n"
        output += "   2. [Сотрудники](#сотрудники)\n"
        output += "      1. [Менеджеры](#менеджеры)\n"
        output += "      2. [Смотрители](#смотрители)\n"
        output += "      3. [Ветеринары](#ветеринары)\n\n"

        output += "# Зоопарк\n\n"
        output += "## Животные\n"

        bird_count = 1
        mammal_count = 1
        predator_count = 1
        herbivorous_count = 1
        reptile_count = 1

        for animal in self.animals:
            if isinstance(animal, Bird):
                output += f"### {bird_count}. Птицы\n" if bird_count == 1 else ""
                output += f"- {animal.alias}, {animal.age} лет, размах крыльев: {animal.wing_span}\n"
                bird_count += 1
            elif isinstance(animal, Mammal):
                output += f"### {mammal_count}. Млекопитающие\n" if mammal_count == 1 else ""
                if isinstance(animal, Predator):
                    output += f"#### {predator_count}. Хищники\n" if predator_count == 1 else ""
                    output += f"- {animal.alias}, {animal.age} лет, тип шерсти: {animal.fur_type}, клыки: {animal.fangs}\n"
                    predator_count += 1
                elif isinstance(animal, Herbivorous):
                    output += f"#### {herbivorous_count}. Травоядные\n" if herbivorous_count == 1 else ""
                    output += f"- {animal.alias}, {animal.age} лет, тип шерсти: {animal.fur_type}, рога: {animal.horns}\n"
                    herbivorous_count += 1
                else:
                    output += f"- {animal.alias}, {animal.age} лет, тип шерсти: {animal.fur_type}\n"
                mammal_count += 1
            elif isinstance(animal, Reptile):
                output += f"### {reptile_count}. Рептилии\n" if reptile_count == 1 else ""
                output += f"- {animal.alias}, {animal.age} лет, тип кожи: {animal.skin_type}\n"
                reptile_count += 1

        output += "\n## Люди\n"

        visitor_count = 1
        employee_count = 1
        manager_count = 1
        zookeeper_count = 1
        veterinarian_count = 1

        for person in self.people:
            if isinstance(person, Visitor):
                output += f"### {visitor_count}. Посетители\n" if visitor_count == 1 else ""
                output += f"- {person.name}\n"
                visitor_count += 1
            elif isinstance(person, Employee):
                output += f"### {employee_count}. Сотрудники\n" if employee_count == 1 else ""
                if isinstance(person, Manager):
                    output += f"#### {manager_count}. Менеджеры\n" if manager_count == 1 else ""
                    output += f"- {person.name}\n"
                    manager_count += 1
                elif isinstance(person, ZooKeeper):
                    output += f"#### {zookeeper_count}. Смотрители\n" if zookeeper_count == 1 else ""
                    output += f"- {person.name}\n"
                    zookeeper_count += 1
                elif isinstance(person, Veterinarian):
                    output += f"#### {veterinarian_count}. Ветеринары\n" if veterinarian_count == 1 else ""
                    output += f"- {person.name}\n"
                    veterinarian_count += 1
                employee_count += 1

        return output

