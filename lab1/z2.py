# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input("Unesi broj: "))

if num == 0:
    print(f"Vaš broj je nula")
elif num % 4 == 0:
    print(f"Broj {num} je djeljiv s 4")
elif num % 2 == 0:
    print(f"Broj {num} je paran")
else: 
    print(f"Broj {num} je neparan")

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

check = int(input("Unesi broj s kojim ćemo dijeliti: "))

if num % check == 0:
    print(f"{num} je dijeljiv sa {check}")
else:
    print(f"{num} nije dijeljiv sa {check}")