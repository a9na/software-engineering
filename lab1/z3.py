# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Instead of printing the elements one by one, make a new list that has all the elements 
# less than 5 from this list in it and print out this new list.

new_list = []

for i in range(len(a)):
    if a[i] < 5:
        # print(a[i])
        new_list.append(a[i])
print(new_list)

for el in a:
    if el < 5:
        new_list.append(el)
print(new_list)

# List comprehension example

new_list = [ el for el in a if el < 5 ]
print(f"List comprehension: {new_list}")

# Ask the user for a number and return a list that contains only elements 
# from the original list a that are smaller than that number given by the user.

lessNums =[]

num = int(input("Enter a number: ")) 
for n in a:
    if n < num:
        lessNums.append(n)
        lessNums.sort() 
print(lessNums)
