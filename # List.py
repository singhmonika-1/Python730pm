# List
# A list in Python is an ordered, mutable(changeable) collection of items enclosed in square brackets[]
names = ["Gaurav","Sarita","Sweta","Neha"]
print(names)

num = [20,40,90,60,70]
print(num)

info = ["Amrita", 22, True,"Python"]
print(info)

print(type(names))
x = 10
print(type(x))

print(type(num))

#           0       1       2        3
fruits = ["apple","orange","mango","grapes"]
#         -4        -3        -2        -1


print(fruits)

print(fruits[0])

print(fruits[3])

print(fruits[-3])
print(fruits[-4])

# len function is used to find the number of items in a list
print(len(names))
print(len(fruits))

print(len(names)-1) # len-1 always prints the last index no.
print(len(fruits)-1)

# To check membership of the element
print("apple" in fruits) # in operator is used to check the membership of the list. It is case-sensitive
print("Apple" in fruits)



