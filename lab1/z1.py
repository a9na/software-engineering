# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 

name = input("Unesi ime: ")
age = input("Unesi godine: ")

year_at_100 = 2024 - int(age) + 100

if year_at_100 <= 2024: 
# print(name, age, year_at_100)
    print("Pozdrav %s, godine %d imao si 100 godina"%(name, year_at_100))
else:
    print(f"Pozdrav {name}, godine {year_at_100} imat ćeš 100 godina")