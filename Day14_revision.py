# Arithmetic operators +,-,%,/,*

print(8+2)
print(8-2)
print(8*2)
print(8/2)
print(8%3)
print(8//3) # It removes the decimal part(floor-division operator)
print(8**2)

# comparison operator ==, != , < ,> ,<=, >=

print(4 == 4)
print(5 == 3)

print(5 != 4)  # != ---- Not equal to
print(5 != 5)

print(4 >3)
print(3 > 4)

print(4 >= 4)
print(5 >= 3)

print(6 <= 6)
print(6 <= 3)


# Logical operators --- and, or ,not
# and operator
print( 4 == 4  and 4 > 3)
#      True    and  True     --- True

print( 4 >3 and 4 >6)
#     True  and   False      ---- False

print(5 != 5 and 5 > 2)
#     False  and  True     ----- False

print(9 > 10 and 4 > 7)
#     False  and   False     ----- False


# Table (AND)
# Condition 1        Condition2          output
# True                 True              True
# True                 False             False
# False                True              False
# False                False             False

# If any condition is False then output is False
# If all the conditions are True then output is True


# OR Operator

print(4 == 4 or 4 != 3)
#      True  or   True    ---- True

print(4 ==4 or 4 > 5)
#     True  or    False   ---- True

print(4 != 4 or 4 >=4)
#     False  or  True    ----- True

print(4 != 4 or 4 >6 )
#     False  or  False    ---- False



