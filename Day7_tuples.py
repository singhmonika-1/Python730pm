# Tuples
# Tuple is an ordered and immutable(unchangeable) collection of elements in Python.
# defining a tuple
t = (10,20,30,40,50)
print(t)
print(type(t))

r =10
print(type(r))

h = "Python"
print(type(h))

t1 = (30)
print(type(t1))

#defining a single element in a tuple
t2 = (30,)
print(type(t2))

t3 = 50,
print(type(t3))

# does tuple stores element by index -- yes
names = ("Sarita","Viha","Riya","Ankit")
print(names[1])
print(names[0])

names1 = ("Sarita","viha","Sarita","Meena","Ram","Ram")
print(names1)                                          # Tuples can store duplicate elements

names2 = [10,20,40,60]
names2[0] = 100
print(names2)

# t6 = (50,70,90,32,54)
# t6[0] = 200
# print(t6)   # tuple does not support item assignment

fruits = ("apple","mango","grapes","banana")
#for
# for item in fruits:
#     print(item)

# for range
for x in range(4):
    print(x)    
    print(fruits[x])

#len function
print(len(fruits))    


# while
i1 = 0
while i1<len(fruits):
    print(fruits[i1])
    i1 =i1+1

# checking membership of elements
print("apple" in fruits)    
print("Mango" in fruits) # 'in' operator is case-sensitive

