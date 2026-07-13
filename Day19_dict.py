# Dictonary
l = ["Rahul",30,56,"Rao","Python"]
print(l[0])

#          Key       :  value
info = {"First Name" : "Amrita",
        "Last Name" : "Sharma",   # Property :value
        "Age" : 25}

print(info)

print(type(info))
print(l[0])

# print(info[0])
#Does dictionary stores element by index no.  --- No

print(info["First Name"])

t = (10,20,30)
print(type(t))
print(type(l))
print(type(info))

# Retrieve
info1 = { "Emp Name" : " Priya Rao",
         "Salary":  30000,
         "Age" : 26,
         "Age" : 25}
print(info1)
print(info1["Emp Name"])
print(info1["Age"])

# Duplicacy in dictionary
print(info1)# In case of duplicate value it takes last key-value pair.

#Update
Vehicle = { "Color" : "Violet",
           "Type" : "Sedan",
           }

Vehicle["Color"] = "White"
print(Vehicle)

Vehicle["Type"] = "SUV"
print(Vehicle)

# Adding a new key- value pair
Vehicle["Car No"] = 1234
print(Vehicle)

print(info.get("Color")) # None

print(Vehicle.get("Color"))# white
print(Vehicle["Color"]) #white
print(Vehicle.get("City")) # the purpose of get() is that it does not crash if the key is missing, it returns None.
# print(Vehicle["City"])

# loop
info3 = { "Student Name" : "Riya Singh",
         "Subject" : "Python",
         "Gender" : "Female",
         "City" : "Pune"}
print(len(info3))  #4

for x,y in info3.items():
    print(x,y)

for x in info3:
    print(x)  # It returns keys of info3
    print(info3[x])  # It returns values of info3