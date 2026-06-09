#List
# A list is an ordered, mutable(changeable) collection of items.
x =10
print(type(x))
y = "Python"
print(type(y))
fruits = [ "Apple","Grapes","Mango","Orange"]
print(fruits)
print(type(fruits))

e = len(fruits)
print(e)
print(len(fruits))

print(len(fruits)-1)

# to check membership of the element
print("Apple" in fruits)
print("apple" in fruits)

# Retrieve the value from the list
names = ["Sweta","Neha","Viha", "Sarita"]
print(names[1])

print(names[3])

print(names[-1])

print(names[-2])


# update the values in the list
names[1] = "Amrita"

print(names)

names[2] = "Pooja"
print(names)

cities = ["Delhi","Pune","Mumbai","Agra"]

# for loop
for item in cities:
    print(item)

    