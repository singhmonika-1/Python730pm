#fromkeys()
w = dict.fromkeys(["one","two","three"])
print(w)

w1 = dict.fromkeys(["one","two","three"],100)
print(w1)

w2 = dict.fromkeys(["one","two","three"])
w2["one"] = 10
w2["two"] = 20
w2["three"] = 30
print(w2)

w3 = dict.fromkeys(["one","two","three"],[100,200,300])
print(w3)

info = { "Name" : "Pooja",
        "Acc no" : 1234,
        "Type" : "Saving"
        }
print(info)

info2 = info
print(info2)

info["Name"] = "Sarita"
print(info)
print(info2)

# copy()
v = { "Color" : "Red",
     "Type" : "Bike",
     "No" : 1234
     }
print(v)
V2 = v.copy()
print(V2)
V2["Color"] = "Green"
print(v)
print(V2)

info3 = [ {"First Name" : "Pooja",
           "Last Name" : "Sharma"},
           {"First Name" : "Riya",
           "Last Name" : "Singh"},
           {"First Name" : "Rahul",
           "Last Name" : "Rao"}
           ]
print(info3)

for item in info3:
    print(item.get("First Name")+" "+item.get("Last Name"))
    item["City"] ="Pune"
print(info3)    


info4 = [ {"First Name" : "Pooja",
           "Last Name" : "Sharma"},
           {"First Name" : "Riya",
           "Last Name" : "Singh"},
           {"First Name" : "Rahul",
           "Last Name" : "Rao"}
           ]
Cities = [ "Pune","Mumbai","Delhi"]

for item,city in zip(info4,Cities):
    item["city"] = city
print(info4)    