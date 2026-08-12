# Exception Handling
# Handling runtime errors so that the program does not terminate unexpectedly.
#prog1
# try:
#     print(10/0)
# except:
#     print("zero division error")
# print("Hello")        


# #prog2

# try:
#     num = int(input("Enter a number"))
#     result = 100/num
#     print(result)

# except ValueError:
#     print("Please enter numbers only")

# except ZeroDivisionError:
#     print("Number cannot be zero")

#try:
#    #code that may cause an exception
#except:
#    #code to handle exception

#Raise : raise is used when we deliberately create an exception.

#Prog3
# age = 30
# if age <= 18:
#     raise Exception("You are not eligible to vote")
# print("You can vote")

# print("Hello")

#marks validation
marks = 200
try:
    if marks < 0 or marks >100:
        raise ValueError("Marks must be between 0 and 100")
    print("Valid marks")

except ValueError as e:
    print("Error:",e)    
    

# OOPs --- Object Oriented Programming
class Person:
    fn = None
    ln = None
    def display_Name(self):
        print(self.fn+self.ln)

monika = Person()
print(monika.fn)    
monika.fn = "Monika" 
print(monika.fn)   


