import tkinter as tk
from tkinter import ttk
from animal import Bird, Mammal, Reptile, Predator, Herbivorous
from people import Visitor, Employee, Manager, ZooKeeper, Veterinarian
from zoo import Zoo

class ZooApp:
    def __init__(self, master):
        self.master = master
        master.title("Zoo Management System")

        self.zoo = Zoo()
        self.create_objects()

        self.create_widgets()

    def create_objects(self):
        self.zoo.add_animal(Bird("Sparrow", 1, "Small"))
        self.zoo.add_animal(Mammal("Lion", 5, "Golden"))
        self.zoo.add_animal(Reptile("Snake", 2, "Scaly"))
        self.zoo.add_animal(Predator("Tiger", 8, "Striped", "Sharp"))
        self.zoo.add_animal(Herbivorous("Elephant", 12, "Gray", "Large"))

        self.zoo.add_person(Visitor("Eve"))
        self.zoo.add_person(Employee("Bob", "Zookeeper"))
        self.zoo.add_person(Manager("Alice"))
        self.zoo.add_person(ZooKeeper("John", "Zookeeper"))
        self.zoo.add_person(Veterinarian("Emily", "Veterinarian"))

        self.zoo.save_zoo("zoo.txt")

    def create_widgets(self):
        self.filter_label = tk.Label(self.master, text="Filter by:")
        self.filter_label.grid(row=0, column=0)

        self.filter_var = tk.StringVar(self.master)
        self.filter_var.set("All")  # default value

        self.filter_options = ["All", "Animals", "People", "Bird", "Mammal", "Reptile", "Predator", "Herbivorous",
                               "Visitor", "Employee", "Manager", "ZooKeeper", "Veterinarian"]
        self.filter_menu = ttk.Combobox(self.master, textvariable=self.filter_var, values=self.filter_options)
        self.filter_menu.grid(row=0, column=1)
        self.filter_menu.bind("<<ComboboxSelected>>", self.update_display)

        self.display_label = tk.Label(self.master, text="Zoo Inhabitants:")
        self.display_label.grid(row=1, column=0, columnspan=2)

        self.display_text = tk.Text(self.master, wrap=tk.WORD)
        self.display_text.grid(row=2, column=0, columnspan=2)

        self.update_display()

    def update_display(self, event=None):
        self.display_text.delete("1.0", tk.END)
        filter_choice = self.filter_var.get()

        if filter_choice == "All":
            formatted_list = self.zoo.get_formatted_zoo_list()
            self.display_text.insert(tk.END, formatted_list)
        elif filter_choice == "Animals":
            for item in self.zoo.animals:
                self.display_text.insert(tk.END, str(item) + "\n")
        elif filter_choice == "People":
            for item in self.zoo.people:
                self.display_text.insert(tk.END, str(item) + "\n")
        else:
            for item in self.zoo.animals + self.zoo.people:
                if item.__class__.__name__ == filter_choice:
                    self.display_text.insert(tk.END, str(item) + "\n")

root = tk.Tk()
app = ZooApp(root)
root.mainloop()
