# Filter function
marks = [44,55,77,99,56]
R = filter(lambda x :x>50,  marks)
print(R)
print(list(R))

T = [100,-45,40,66,-55]

#deposit
R1 = list(filter(lambda x : x>0 , T))
print(R1)

# withdrawl
R2 = list(filter(lambda x :x<0, T))
print(R2)

# Map function
# map() is used to perform the same operation on every element of a collection without using a loop

#Multipy by 2
numbers = [2,4,6,8]
t1 = list(map(lambda x : x*2 ,numbers))
print(t1)

# using normal function
def multiply(x):
    return x*2

r3 = list(map(multiply,numbers))
print(r3)

# find age
birthYear = [2000,1999,2005,2008]
t5 =list(map(lambda x : 2026-x ,birthYear))
print(t5)

# Reduce function



from functools import reduce

sum = [10,20,30,40,50]
y = reduce(lambda x,y : x+y ,sum)
print(y)

Num = [2,3,4,5]
t7 = reduce(lambda x,y : x*y, Num)
print(t7)





























































# | Feature                       | `map()`                                | `filter()`                                     |
# | ----------------------------- | -------------------------------------- | ---------------------------------------------- |
# | **Purpose**                   | Transforms (modifies) every element    | Selects only elements that satisfy a condition |
# | **Returns**                   | A new iterable with transformed values | A new iterable with filtered values            |
# | **Function should return**    | Any value                              | `True` or `False`                              |
# | **Number of output elements** | Same as input                          | Can be fewer than input                        |
# | **Use when**                  | You want to change each element        | You want to remove unwanted elements           |