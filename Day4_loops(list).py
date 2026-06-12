#List
# while loop

cities = ["Mumbai","Pune","Jaipur","Mysore","Agra"]

# for x in cities:
#     print(x)

# for x in range(5):
#     print(x)
#     print(cities[x])    

# for x in range(len(cities)):
#     print(cities[x])

# while loop
i1 = 0
while i1<5:
    print(cities[i1])
    i1 = i1+1

names = ["Sarita","Anita","Viha","Priya"]
i1 = 0
while i1<4:
    print(names[i1])
    i1 = i1+2

i1 =0
while i1<len(names):
    print(names[i1])
    i1 = i1+1    

fruits = ["apple","mango","guava","watermelon"]   
i1 =0
while i1<len(fruits):
    print(fruits[i1])
    i1 = i1+1

# append
fruits.append("pineapple")

print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)
