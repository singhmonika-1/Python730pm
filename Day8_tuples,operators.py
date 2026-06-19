t = (10,20,30)
print(t)

print(type(t))

# t[0] = 100
# print(t) # tuple does not support item assignment

# unpacking
j =(11,22,33,44,55)
j1,j2,j3,j4,j5 = j
print(j1)
print(j2)
print(j4)

# Methods
#count
num = (11,22,33,44,55,11,33)
e = num.count(11)
print(e)

e1 = num.count(22)
print(e1)

#index
num1 = (11,22,33,44,55,66,44,88,11,11,22,44)
r1 = num1.index(11)
print(r1)

r2 = num1.index(11,7)
print(r2)

r3 = num1.index(44,4,9)
print(r3)

tup = (20,30,40)
print(tup)

# del tup
# print(tup)

# Arithmetic Operator
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
c =11
d = 2
print(c%d) # Modulus operator
print(c//d)# floor division operator

r =2
t = 3
print(2**3)
print(r**t) #  power

print(34+22)
print(22/11)