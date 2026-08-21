# Prog 2
class FatherA:
    def __init__(self,fn,ln):
        print("Father constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName)
        print(self.lastName)

class MotherA:
    def __init__(self,age):
        print("Mother constructor called")
        self.Age = age

    def displayAge(self):
        print(self.Age)

class SonA(MotherA,FatherA):
    def __init__(self,age,fn,ln,ssn):
        super().__init__(age)
        self.sname = ssn

        FatherA.__init__(self,fn,ln)  #Explicitly call Father constructor

    def displaySname(self):
        print(self.firstName+" "+self.sname)

s2 = SonA(39,"Mukesh","Mishra","Mukul")       

s2.displayAge()
s2.displayFName()
s2.displaySname()

# Hierarchical Inheritance

# Multiple child classes inherit from the same sinlge parent class.

#Prog 1
#Parent class
class Father:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName+" "+self.lastName)

#child class1
class Son(Father):
    def __init__(self,fn,ln,ssn):
        super().__init__(fn,ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname+" "+self.lastName)   

#child class2
class Daughter(Father):
    def __init__(self,fn,ln,dfn):
        super().__init__(fn,ln)
        self.dname = dfn

    def displayDName(self):
        print(self.dname+" "+self.lastName)  

s2 = Son("Mukesh","Sharma","Rahul")   
s2.displayName()    #Mukesh Sharma
s2.displaySName()     #Rahul Sharma

d1 = Daughter("Mukesh","Sharma","Sarita")
d1.displayName()#Mukesh Sharma
d1.displayDName()#Sarita Sharma
            





# Method Resolution order
# MRO tells Python the order in which it searches classes for a method or attribute
# Method Resolution Order (MRO) is the order in which Python searches for a method or attribute in a hierarchy of classes
# when there is multiple inheritance.

#Prog3

class Father2:
    def show(self):
        print("Father")

class Mother2:
    def show(self):
        print("Mother")

class Child2(Father2,Mother2):
    pass                

c = Child2()
c.show() #Father
          # Child2 ---Fahter2----Mother2


class Father2:
    def show(self):
        print("Father")

class Mother2:
    def sow(self):
        print("Mother")

class Child2(Father2,Mother2):
    pass                

c1 = Child2()
c1.sow() 