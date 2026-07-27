# conditional statement
# conditional statements are decision -making statements in Python. They allow a program to execute different blocks of
# code based on whether condition is True/False.
 
# if condition:
#    statements


marks = 60
if marks >= 33:
    print("You passed the test")


#if condition:
#    statement
#else:
#    statement

age = 17

if age >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# if condition:
#   statement
# elif condition:
#   statement
# elif condition:
#   statement
# else 
#   statement

Marks = 82

if Marks >=90:
    print("Grade = A")
elif Marks >=75:
    print("Grade = B")
elif Marks >=60:
    print("Grade = C")    
else:
    print("Grade = D")    

# Nested if statement

age = 25
citizen = True
if age >=18:
    if citizen:
        print("Eligible to vote")    


# Logical operators
# We can combine multiple conditions using logical operators

#and
age = 18
salary = 50000

if age >=18 and salary >=20000:
    print("Loan apporoved")
else:
    print("Loan is not approved")    

#or
marks = 35
sports = True

if marks >=40 or sports:
    print("Eligible for the next exam")
else:
    print("Not eligible the next exam")    

# not
# reverse the result

is_logged_in = True

if not is_logged_in:
    print("Please log in")
else:
    print("You're already logged in")    



