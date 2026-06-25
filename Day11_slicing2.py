# slicing
# [start:stop:step]
# start = Index from where slicing begins((included)
# stop = Index where slicing ends(excluded)
# step = No. of positions to move each time ( by default =1)

# slicing in list

#           0       1       2       3       4
names = ["Sarita","Gaurav","Viha","Priya","Riya"]
#           -5      -4      -3      -2      -1

print(names[0:3:1])  
print(names[ :3])
print(names[:5:2])
print(names[1: :2])
print(names[2:])
print(names[:]) # prints the list
print(names[::-1]) # prints the reverse list
print(names[: :]) #print the list

print(names[-5:-2])
print(names[-2:-4])
print(names[-2:-4:-1])# start index must come befor end index.

# slicing in string
city = "chandrapur"

#  0    1    2    3     4    5    6    7    8    9
#  c    h    a    n     d    r    a    p    u    r
# -10  -9   -8   -7    -6   -5   -4   -3   -2   -1

print(city[:9])
print(city[3::])
print(city[3:7])
print(city[::-1])
print(city[1:10:2])