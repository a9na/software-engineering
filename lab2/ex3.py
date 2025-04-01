import csv

with open('c:/Users/student/Documents/softEng/se-labs-2425-sr/lab2/ex2-text.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    employees = []
    for row in reader:
        employee, job_title, age, office = row
        employees.append(f"employee: {employee},title: {job_title},age: {age},office: {office}")

print(employees)