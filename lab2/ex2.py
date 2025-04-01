import csv

with open('c:/Users/student/Documents/softEng/se-labs-2425-sr/lab2/ex2-text.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    employees = []
    locations = []

    for row in reader:
        employee, job_title, age, office = row
        employees.append(f"{employee},{job_title}")
        locations.append(f"{employee},{office}")

with open('ex2-employees.txt', 'w') as emp_file:
    for emp in employees:
        emp_file.write(emp + '\n')


with open('ex2-locations.txt', 'w') as loc_file:
    for loc in locations:
        loc_file.write(loc + '\n')
