# functions
# function without parameter and with return type

def get_numb():
    return 100

e = get_numb()
print(e)


def get_message():
    return "Hello World"

e1 = get_message()
print(e1)

# Integer as a parameter and integer as a return type
def add1(x,y):
    return x+y

e2 =  add1(12,3)
print(e2)
print(type(e2))

# float as a parameter and float as a return type
def subt(x,y):
    return x-y
e3 = subt(20.9,10.4)
print(e3)
print(type(e3))

# Boolean as a parameter and boolean as a return type

def can_drive(age,have_vehicle):
    if age >= 18 and have_vehicle:
        return True
    else: 
        return False

f = can_drive(22,True)    
print(f)
print(type(f))

# string as a parameter and string as a return type
def greet(word):
    return "Good" + word

s = greet("  morning")
print(s)

s1 = greet(" Evening")
print(s1)
print(type(s1))

#list as a parameter and list as a return type
def addElement(lst,name):
    lst.append(name)
    return lst

l = ["Roopa","Shweta","Viha"]
t = addElement(l,"Pooja")
print(t)
print(type(t))

l1 = ["Priya","Deepti","Ram"]
t1 = addElement(l1,"Amit")
print(t1)
print(type(t1))

# tupe as a parameter and tuple as a return typ
def tup1(t):
    return t

t1 = (11,22,33,44,55)
t5 = tup1(t1)
print(t5)
print(type(t5))





