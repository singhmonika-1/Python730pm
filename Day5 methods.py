# List
# creating a list
fruits = ["Mango","Banana","Apple","Grapes","Guava"]
# print(fruits)

# # Checking the data type of a list
# print(type(fruits))

# # Accessing List Elements using Indexing
# print(fruits[0])
# print(fruits[3])

# # Updating (Modifying) a list element
# fruits[1] = "Pineapple"
# print(fruits)

# # Finding the length of list
# print(len(fruits))

# # Membership Operator (in)
# # Check if an item exists
# print("Apple" in fruits)

# # case senstivity example
# print("apple" in fruits)

# # finding the last index position
# print(len(fruits)-1)

# # for loop
# for item in fruits:
#     print(item)

# # for loop with range()
# for x in range(len(fruits)):
#     print(fruits[x])

# while loop
i1 =0
while i1<len(fruits):
    print(fruits[i1])
    i1 =i1+1

# Python list methods
cities = ["Jaipur","Kolkata","Pune","Mumbai","Mysore"]
print(cities)

#Append() ---Add element at the end of the list
cities.append("Delhi")
print(cities)

# pop() method--- Remove the last element
cities.pop()
print(cities)

cities.pop(1)
print(cities)

# Insert() method--- Insert element at a specific position
cities.insert(0,"Nagpur")
print(cities)

cities.insert(2,"Agra")
print(cities)

# remove() method-----Remove the element by value
cities.remove("Jaipur")
print(cities)

# clear() method -----Remove all the element
cities.clear()
print(cities)