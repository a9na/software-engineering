a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

with open("lab1/numbers.txt" , "r") as f:
    nums = f.read()

# a = []
# for x in nums.split(","):
#    a.append(int(x))
# print(a)

a = [ int (x) for x in nums.split(',') ]

# kvadrat svakog elementa
res = [ x**2 for x in a ]
print(res)

# res = []
# for x in a:
#   res.append(x**2)
#print(res)