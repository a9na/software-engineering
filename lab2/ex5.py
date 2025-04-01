import json

class Employee:
    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"

with open("ex4-employees.json", "r", encoding="utf-8") as f:
    employees = json.load(f)

employees_list = []

for emp_data in employees:
    employee = Employee(
        name=emp_data['employee'],
        title=emp_data['title'],
        age=emp_data['age'],
        office=emp_data['office']
)
employees_list.append(employee)

for e in employees_list:
    print(e)
