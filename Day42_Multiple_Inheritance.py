# Multiple Inheritance : One child class inherits from more than one parent class.
#Parent class1
class Father:
    def __init__(self,fn,ln):
        print("Father constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName)
        print(self.lastName)

#Parent class2
class Mother:
    def __init__(self,fn,ln):
        print("Mother constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName)
        print(self.lastName)

#Child class
class Son(Father,Mother):
    def __init__(self,fn,ln,sfn):  # son--- Father ---Mother--obj
        super().__init__(fn,ln)
        self.sname = sfn

    def displaySName(self):
        print(self.firstName+"  "+self.sname)

s1 = Son("Mahesh","Sharma","Ravi")
s1.displaySName()
s1.displayMName()
s1.displayFName()


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

        FatherA.__init__(self,fn,ln)

    def displaySname(self):
        print(self.firstName+" "+self.sname)

s2 = SonA("Mukesh","Mishra",39,"Mukul")       

s2.displayAge()
s2.displayFName()
                        


           