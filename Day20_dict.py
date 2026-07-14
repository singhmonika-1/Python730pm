# Loops in dictionary
Bank = { "Name" : "Amrita",
        "Acc No" : 1234,
        "Type" : "Saving"}
#       Key    : value
#     Property : value
print(len(Bank))# 3

for x in Bank:
    # print(x)
    print(Bank[x])

for key in Bank.keys():
    print(key)  

for value in Bank.values():
    print(value)     

for x,y in Bank.items():
    print(x,y)    

# Retrieve
print(Bank["Name"])    
print(Bank["Acc No"])
# get
info = {"First Name" : "Sarita",
        "Last Name" : "Rao",
        "Age" :23}
# print(info["City"])

print(info.get("City"))  #none
print(info.get("Age"))

# Update
info["City"] = "Pune"
print(info)

info["Age"] = 22
print(info)

#update
info.update({"Gender" : "Female"})
print(info)

# Delete
info.popitem()# It will delete the last item
print(info)

info.pop("Age")
print(info)

info.clear() # It will empty the dictionary
print(info)

info_2 = { "First Name" : "Sarita",
          "Last Name": "Sharma"}
del info_2  # It will delete the whole dictionary with memory
# print(info_2) 

# Setting default value for key
Vehicle = { "color" : "Red",
           "type" : "Sedan"
           }

e = Vehicle.setdefault("type","SUV")# if the key exists,it returns the existing value
print(e)
print(Vehicle)
e1 = Vehicle.setdefault("Car No", 123)#If the key does not exists, it add the key with the given default value and returns the value.
print(e1)
print(Vehicle)
print(len(Vehicle))

# fromkeys()
w = dict.fromkeys(["one","two","three"])#The fromkeys() method creates a dictionary with the specified keys.If you don't provide a value,
print(w)                            #Python assigns None to every key.

w1 = dict.fromkeys(["one","two","three"],100)# Every key gets the value 100.
print(w1)