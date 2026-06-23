# Slicing in list

# [start:stop:step]

# start: Index from where slicing begins(included)
# stop: Index where slicing ends(excluded)
# step : Number of positions to move each time


#          0        1      2         3       4
names = ["Sarita","Viha","Gaurav","Priya","Riya"]
#         -5       -4      -3       -2      -1

print(names[0:4:1])
print(names[0:4])
print(names[0:4:2])
print(names[0:5:2])
print(names[0:2])
print(names[1:5])
print(names[1:5:2])
print(names[:4])
print(names[2:])
print(names[:])
print(names[::2])
print(names[:5:2])
print(names[-5:-2])
print(names[::-1]) # reverse list
print(names[-4:3])