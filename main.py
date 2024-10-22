# main.py
from animal import Bird
from people import Visitor
from zoo import Zoo

def main():
    # Создание зоопарка
    zoo = Zoo()

    # Добавление нового животного и человека в зоопарк
    zoo.add_animal(Bird("Sparrow", 1, "Small"))
    zoo.add_person(Visitor("Eve"))

    # Сохранение информации о зоопарке в файл
    zoo.save_zoo("zoo.txt")

    # Загрузка и отображение информации о зоопарке
    zoo.load_zoo("zoo.txt")

    # Вывод на консоль содержимого файла
    print("\nZoo Data:")
    with open("zoo.txt", "r") as file:
        print(file.read())

if __name__ == "__main__":
    main()
