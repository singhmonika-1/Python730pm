# list comprehension

birthYear = [2000,2001,2002,2003]
ages = []

for x in birthYear:
    ag = 2026- x
    ages.append(ag)
print(ages)   #[26, 25, 24, 23]

#p2
marks = [50,90,91,60,78]
above70 = []

for x in marks:
    if x > 70:
        above70.append(x)
print(above70)             #[90, 91, 78]


# List comprehension
#syntax:
# [expression  loop  condition]
# list comprehension offers a concise way to create a new list using existing iterables

birthYear1 = [2000,2001,2002,2003]

e = [ 2026-x for x in birthYear1]
print(e)         #[26, 25, 24, 23]

marks1 = [50,90,91,60,78]
e1 = [ x  for x in marks1 if x >70]
print(e1)            #[90, 91, 78]

listA = [1,2,3,4,5,6,7,8,9,10]
# [2,4,6]
e3 =[x*2 for x in listA]
print(e3)   #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

names = ["sarita","vikas","gaurav","priya"]

e5 = [x.upper() for x in names]
print(e5)             #['SARITA', 'VIKAS', 'GAURAV', 'PRIYA']

names1 = ["Priya","Sweta","Viha","Amrita"]
# ["P","S","V","A"]
e6 = [x[0]  for x in names1]
print(e6)  #['P', 'S', 'V', 'A']

#Ternary operator: It offers a way to condense an if-else statemnet into a single line.

evenodd = [11,22,44,55]
# [odd,even,even,odd]

e7 = ["even" if x%2 == 0  else "odd" for x in evenodd]
print(e7)  #['odd', 'even', 'even', 'odd']

marks2 = [95,82,67,45,73]
grades = ["A" if m >=90 
          else "B" if m>=75
          else  "C"if m>=60
          else "Fail"
          for m in marks2]
print(grades)
