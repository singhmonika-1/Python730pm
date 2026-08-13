age = 30
if age <= 18: 
          raise Exception("You are not eligible to vote")

print("You can vote")

print("Hello")

# using try - except

age = 15
try:
        if age <= 18:
                raise Exception("you are not eligible to vote")
        print("You can vote")
except Exception as e:
        print("Error:",e)

print("Hello")

# OOps

class Person:
        fn = None
        ln = None

        def displayName(self):
                print(self.fn+" "+self.ln)

p = Person()
print(p.fn)  
print(p.ln)              

p.fn = "Priya"
p.ln = "Rao"
print(p.fn) # Priya
print(p.ln)

print(p.displayName())

r = Person()
print(r.fn)            
print(r.ln)    
r.fn = "Rahul"
r.ln = "Sharma"
print(r.fn)  #Rahul
print(r.ln)  #Sharma

class Person2:
        def __init__(self,fn,ln):
                self.firstName = fn
                self.lastName = ln


        def displayName(self):
                print(self.firstName+" "+self.lastName)  

sarika = Person2("Sarika","Mishra")
print(sarika.firstName)     
print(sarika.lastName)       
print(sarika.displayName())          
          
                





