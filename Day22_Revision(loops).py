info =[
    {"first name":"Riya",
     "last name":"Pawar"},
     {"first name": "Vikas",
      "last name":"Singh"},
      {"first name":"Shreya",
       "last name":"Sinha"}
]

for dct in info:
    for x,y in dct.items():  #dct ---dictionary
        print(x,y)           # info--- list



#Loop
# Def : A loop is a programming structure used to repeat a block of code multiple times.
# print "hello"  5 times
# print("hello")

for i in range(5):
    print("Hello")

# types of loops
# for loop
#  while loop
# def of for loop : a for loop is used when we know that how many times we want to repeat something.

# range(stop)
for i in range(5): 
    print(i)    # 0 1 2 3 4

#Parameters
# start : starting value(included)
# stop : Ending value(Excluded)
# step :Increment/decrement

# range(start,stop)
for i in range(2,7):
    print(i)

# range(start,stop,step)
for i in range(1,10,2):
    print(i)    


l = [10,20,30,40]

for x in range(4): 
    print(x)
    print(l[x])   

# tuples


# strings
name = "Vartika"
for x in name:
    print(x)

for x in range(len(name)):
    print(name[x])    


# loops in dictionary
student = {"Name" : "Riya",
           "Age" : 23,
           "City" :"Pune"}    

for key in student:
    print(key)

for value in student.values():
    print(value)    

for x,y in student.items():
    print(x,y)    