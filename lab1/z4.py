# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Unesite broj: "))

list_range = list(range(1,num+1))

djelitelji = []

for el in list_range:
    if num % el == 0:
        djelitelji.append(el)
print(djelitelji)


if len(djelitelji) > 2:
    print("Broj nje prost")
else:
    print("Broj je prost")