import json

class Employee:
    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"

    def employ(self, name, title, age, office):
        new_employee = Employee(name, title, age, office)
        self.employees.append(new_employee)

    def fire(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)
                break

    def load_from_json(self, path_to_json):
        with open(path_to_json, "r", encoding="utf-8") as f:
            employees_data = json.load(f)
            for emp_data in employees_data:
                self.employ(emp_data['employee'], emp_data['title'], emp_data['age'], emp_data['office'])

    def save_to_json(self, path_to_json):
        with open(path_to_json, "w", encoding="utf-8") as f:
            employees_data = [
                {
                    "employee": e.name,
                    "title": e.title,
                    "age": e.age,
                    "office": e.office
                }
                for e in self.employees
            ]
            json.dump(employees_data, f, ensure_ascii=False, indent=4)

    def print_employees(self):
        print(f"{self.name}")
        print("-" * len(self.name))
        for i, e in enumerate(self.employees, start=1):
            print(f"{i}. {e}")

def main():
    nike = Company("Nike")
    print(nike)

    nike.employ("Homer Simpson", "CEO", 44, "Lobby")
    nike.employ("Marge Simpson", "CTO", 33, "Lobby")
    print(nike)

    nike.fire("Homer Simpson")
    print(nike)

    adidas = Company("Adidas")
    adidas.load_from_json("ex4-employees.json")
    print(adidas)
    adidas.print_employees()

    adidas.employ("Homer Simpson", "CEO", 44, "Lobby")
    adidas.employ("Marge Simpson", "CTO", 33, "Lobby")
    adidas.employ("Bart Simpson", "CEO", 44, "Lobby")
    adidas.employ("Lisa Simpson", "CTO", 33, "Lobby")
    print(adidas)
    adidas.print_employees()

    adidas.fire("Homer Simpson")
    adidas.fire("Marge Simpson")
    print(adidas)
    adidas.print_employees()

    adidas.save_to_json("ex6-employees.json")

if __name__ == "__main__":
    main()