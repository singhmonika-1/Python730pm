# Function
# set as a parameter and set as a return type
def removeE(seta,e):
    seta.remove(e)
    return seta

setb = {11,22,33,44,55}
r = removeE(setb,33)
print(r)
print(type(r))

#dictionary as a parameter and dictionary as a return type
def addCity(dictA):
    dictA["city"] = "Pune"
    return dictA

info = {"firstName" :"Priya",
        "lastName" : "Rao"}
r1 = addCity(info)
print(r1)
print(type(r1))

#default parameter
def add(x =2, y = 3):
    print(x+y)

add()    
add(7,8)

# Positional arguments
def student(name,age):
    print("Name:",name)
    print("Age:",age)

student(23,"Riya")  
student(age = 21, name = "Pooja")  

#single-astrisk form of args can be used as a parameter to pass ht variable length of arguments to a function
def addAll(*args):
    print(args)
    total = 0
    for x in args:
        total = total +x
    print(total)

addAll(2,7,9,90,78,300,45,23,98,23)    
addAll(4,5,6,7,8,9,10,30,50,60,40,40,30,100,1000,23)    


# **kwargs is used to pass key-value pair .It allows us to pass arguments in the form of key-value pair
#Inside the function,kwargs will be a dictionary containing all the arguments in the form of key-value pair passed to the function

def showInfo(**kwargs):
    print(kwargs)
    kwargs["City"] = "Pune"
    print(kwargs)
    print(type(kwargs))

showInfo(name = "Riya", age = 23 , course = "Data Analysis") 
# showInfo({"name" : "Riya", "age" : 23 , "course" : "Data Analysis"})   TypeError: showInfo() takes 0 positional arguments but 1 was given


