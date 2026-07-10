# Dictionary

l = ["Pooja","Pune",23,50]


#        Key    :    value
info = {"First Name" : "Arti",
        "Last Name" : "Singh",
        "City" : "Pune",
        "Age" : 24}

print(info)

#Dictionary does not store elements by index number.
# print(info[1]) 

# Retrieve
print(info["First Name"])
print(info["City"])
print(info["Age"])

print(info.get("First Name")) # the purpose of get() is that it does not crash if the key is missing. It returns none.
print(info.get("Subject"))
# print(info["subject"])

# Duplicate values in Dictionaries
Vehicle = { "Color" : "Violet",
            "Type" : "Sedan",
            "Color" : " White"}
print(Vehicle)
print(Vehicle["Color"]) # In case of duplicate value in dictionary it takes last key-value pair
print(Vehicle.get("Type"))



# update
Tiger = {"Color" : "Red",
         "City" : "Bengal"}
print(Tiger)

Tiger["Color"] = "Yellow"
print(Tiger)

Tiger["count"] = 40
print(Tiger)

# loop
info1 = {"first name" : "Riya",
         "last name" : "Pawar",
         "city" : "Pune",
         "gender" : "Female"}
 
for x in info1:
    # print(x)
    print(info1[x])

for x,y in info1.items():
    print(x,y)    

Bank = {"Name" : "Ankita",
        "Acc no" : 1234,
        "Type" :"Saving"
        }    

print(Bank)

for key in Bank.keys():
    print(key)

for value in Bank.values():
    print(value)    

print(len(Bank))    





