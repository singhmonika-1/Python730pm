# lambda function
# Lambda function is a small ,anonymous(nameless) function in python that can have any number of parameters but only one expression


def add(x,y):
    print(x+y)

add(2,3)


#lambda function
r = lambda x,y : x+y
print(r(3,4))
print(r(90,100))

#syntax:
# lambda parameters : expression

# to find square of a no.
def sq(x):
    print(x*x)

sq(2)
sq(3)

t1 = lambda x : x*x
print(t1(3))
print(t1(9))

# returning a lambda function
def squrt():
    return lambda x : x*x

f = squrt()  # f = lambda x : x*x   # f store the returned lambda
print(f(6))

# filter function
#filter function is used to select elements from an iterable (such as list,tuple) that satisfy the given condition


numb = [1,2,3,4,5,6]
result = filter(lambda x : x%2 == 0, numb)
print(result)  #<filter object at 0x000001DFA66BB190>
print(tuple(result))
print(list(result))


def is_even(x):
    return x%2 == 0

t2 = list(filter(is_even,numb))
print(t2)





