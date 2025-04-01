import json

employees = []

with open("c:/Users/student/Documents/softEng/se-labs-2425-sr/lab2/ex2-text.csv", "r") as csv_file:
    headers = csv_file.readline().strip().split(',')

    for line in csv_file:
        employee_data = line.strip().split(',')
        employee_dict = {
            'employee': employee_data[0],
            'title': employee_data[1],
            'age': int(employee_data[2]),
            'office': employee_data[3]
        }
        employees.append(employee_dict)

print(employees)

with open("ex4-employees.json", "w", encoding="utf-8") as f:
    json.dump(employees, f, ensure_ascii=False, indent=4)