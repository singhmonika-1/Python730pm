# Exception Handling
# Write program----- Compile-------Run--------Output

# 1.Compile time error /Syntax Error
# 2.Run time error---these type of errors can be handled by try and except
# 3.Logical error


# Compile time error are Syntax error

#Program1
# q1 = 10
# q2 =5
# print(q1+q2)
# if q1>q2
#    print("q1 is greater")
# else:
#    print("q2 is greater")   


# #program2
# print("hello)   SyntaxError: unterminated string literal


# program3

# def add(a,b):
# return a +b     #IndentationError: expected an indented block after function


# Run time error
#prog 4
# def divideA(a,b):
#     return a/b

# e1 = divideA(10,0)
# print(e1)          #ZeroDivisionError: division by zero

# prog5
# numb = [10,20,30,40]
# print(numb[6])   # IndexError: list index out of range

#prog6
# a1 = 100
# a2 = "Hello"
# print(a1+a2)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'



# Logical error
#Prog7
l = 20
b = 10
Area = l+b  # Incorrect formula
print(Area)

#Prog8
age =20
if age <= 18:  #Incorrect condition
    print("Eligible to vote")
else:
    print("Not eligible to vote")  


# Exeception Handling
# handling runtime errors so that program does not terminate unexpectedly.

#try:
      #code that may cause an exception
#except:     
      #code to handle the exception


try:
    print(10/0)

except:
    print("zero division error")

print("Bye")


