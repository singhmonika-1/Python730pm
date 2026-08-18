# Inheritence
# It is a process in which a child class inherits the properties and behaviour(methods) from a parent class.


#single inheritence
#prog1
#Parent class
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName+" "+self.lastName)  

#child class
class Teacher(Student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)      

t1 = Teacher("Shreya","Mishra",10000)

print(t1.firstName)
print(t1.lastName)
print(t1.displayName())

print(t1.salary)
print(t1.displaySalary())

# Multilevel Inheritence

class Grandfather:
    def __init__(self,fn,ln):
        self.firstName = fn  
        self.lastName = ln

    def displayGName(self):
        print(self.firstName+" "+self.lastName) 

class Father(Grandfather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn


    def displayFName(self):
        print(self.fname+" "+self.lastName) 

class Son(Father):
    def __init__(self,fn,ln,ffn,sfn):
        super().__init__(fn,ln,ffn)
        self.sname = sfn

    def displaySName(self):
        print(self.sname+" "+self.lastName) 

s1 = Son("Suresh","Mishra","Shekhar","Harshit")   

print(s1.firstName)
print(s1.lastName)
print(s1.displayGName()) #Suresh Mishra

print(s1.fname)
print(s1.displayFName())

print(s1.sname)
print(s1.displaySName())