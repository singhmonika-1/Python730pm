# Function
# print(3+4)
# print(6+7)
# print(4-3)

# print("Welcome to Python")

# p1
def wel():
    print("Welcome to Python")

wel()
wel()
wel()
wel()

# function :A function is a block of resuable code that performs a specific task.
# Instead of writing the same code multiple times, we write it once inside a function and call it whenever we need it.

# function without parameter and without return type
def add():
    print(9+9)
    print("Hello, how are you?")

add()   
add() 

def student_info():
    print("Name :Priya")
    print("Course : Data Analysis")
    print("City : Pune")

student_info()    
student_info()

# function with parameter and without return type
def Cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)

Cal(20,3)    
Cal(100,6)


def area(length,breadth):
    print("Area = ", length*breadth)

area(10,20)    
area(40,30)

# function with parameter and with return type

def percentage(english,maths,science):
    total = english + maths + science
    per = total/3
    return per

s1 = percentage(78,89,90)
print(s1)

s2 = percentage(90,95,80)
print(s2)




