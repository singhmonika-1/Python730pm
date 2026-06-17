# methods
#append
fruits = ["Apple","Pineapple","Orange","Guava"]
# fruits.append("Grapes")
# print(fruits)

# #pop
# fruits.pop()
# print(fruits)

# fruits.pop(1)
# print(fruits)

# #insert
# fruits.insert(0,"Watermelon")
# print(fruits)

# #remove
# fruits.remove("Orange")
# print(fruits)

#count()--- It is used to count the no. of occurrences of a particular element

num =[11,22,33,44,22,66,11,22,22]
e = num.count(11)
print(e)


e1 = num.count(22)
print(e1)

num1 = [11,22,33,44,55,66,44,77,33,44,66,55,66,33]

# index()----It returns the index no. of a particular element

e3 = num1.index(33)# return the index no. of  first occurrence of the element.
print(e3)

e4 = num1.index(66)
print(e4)

e5 = num1.index(33,3) # returns the index no. of 33 after 3rd index no.
print(e5)

e6 = num1.index(33,3,9)
print(e6)

#sort()

num1.sort()
print(num1)

fruits.sort()
print(fruits)

#extend()--- It is used to add multiple elements
fruits1 = ["Apple","Banana"]
fruits2 = ["Mango","Guava"]
fruits1.extend(fruits2)
print(fruits1)

cities = ["Delhi","Mumbai"]
cities1 = ["Pune","Jaipur"]
cities.append(cities1)
print(cities)

