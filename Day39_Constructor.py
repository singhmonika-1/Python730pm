# Constructor
# A constructor in Python is a special method that is automatically called when you create an object from a class.
# A constructor is defined using the __init__()method.
# A class can have only one __init__()method.

# A constructor is used to initialize when the object is created.

# class ClassName:
#       def __init__(self,parameters):
#            self.attribute = parameters
# 

class Person1:
    def __init__(self,n,a):
        self.name = n         #properties : name,age
        self.age  = a

P1 = Person1("Harshita",20)
print(P1.name)
print(P1.age)



#prog 2
class Person2:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName+" "+self.lastName)  

s1 = Person2("Sarika","Rao")   
print(s1.firstName)
print(s1.lastName)
print(s1.displayName())


#Prog3
class Person3:
    #constuctor
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    #instance method
    def displayName(self):
        return self.firstName+" "+self.lastName
    #instance method
    def updateFirstname(self,nfn):
        self.firstName = nfn
        return self.firstName

r1 = Person3("Pooja","Deshpande")
r2 = Person3("Priya","Rao")
print(r1.firstName)
print(r1.lastName)
print(r1.displayName())
print(r1.updateFirstname("Pooja D"))

print(r2.firstName)#Priya
print(r2.lastName)  #Rao
print(r2.displayName()) # Priya Rao
print(r2.updateFirstname("Priya R")) # Priya R
   
    


