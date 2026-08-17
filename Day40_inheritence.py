# Class Variable : A class variable is a variable that belongs to the class itself,rather than to a particluar object

#prog1
class Person:
    #class variable
    country = "India"

    def __init__(self,name,age):
        self.Name = name
        self.Age = age

p1 = Person("Amrita",29)
p2 = Person("Pooja",25)   

print(p1.Name)
print(p1.Age)
print(p1.country)

print(p2.Name)
print(p2.Age)
print(p2.country)

p3 = Person("Riya",20)
print(p3.Name)
print(p3.Age)

p3.country = "INDIA"   # p3 gets its own instance variable
print(p3.country)

print(Person.country) #India


#class method

# prog2
class Person1:
    country = "India"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(Person.country)
        return self.firstName+" "+self.lastName

    @classmethod
    def updateCountry(cls,ucountry):
        Person1.country = ucountry

t1 = Person1("Shreya","Singh")
t2 = Person1("Sunil","Mane")  

print(t1.firstName)
print(t1.displayName())
print(t1.country)

t1.country = "INDIA"
print(t1.country)

Person1.updateCountry("Bharat")
print(Person1.country)

print(t1.country)
print(t2.country)

t3 = Person1("Amit","Sharma")
print(t3.country)

# single inheritence
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName+" "+self.lastName)


class Teacher(Student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl

def displaySalary(self):
    print(self.salary)     


s1 =Teacher("priya","Rao",10000)    
print(s1.firstName)            #priya   




























# Class variable   vs  Instance variable

# Class Variable	                           Instance Variable
# Belongs to the class	                       Belongs to a particular object
# Shared by all objects                        Separate for each object
# Defined directly inside the class	           Usually defined using self
# Example: country = "India"	               Example: self.name = name