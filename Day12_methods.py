# [start:stop:step]
# start---Index from where slicing begins(included)
# stop --- Index where slicing ends (excluded)
# step --- Number of positions to move each time
#          0      1         2      3       4
names = ["Sarita","Pooja","Rita","Priya","Riya"]
#         -5      -4       -3      -2      -1

print(names[0:3])
print(names[:4])
print(names[1:5:2])
print(names[2:])
print(names[:])# print the list
print(names[4:1:-1])
print(names[1:4:-1])
print(names[::-1]) #Reverse list
print(names[-1:-5:-1])
print(names[-1:1:-1])
print(names[1:-2])

city = "chandrapur"
#  0  1   2   3    4   5  6   7   8    9
# c   h   a   n   d   r   a   p   u    r
#-10  -9  -8  -7  -6  -5  -4 -3  -2   -1

print(city[:4])
print(city[3::])
print(city[2:9:2])
print(city[::-1])
print(city[1:10:2])

# Methods of string
fn = "Python"
print(fn)
print(type(fn))

e = fn.lower()# It converts the string into lower-case
print(e)

e1 = fn.upper() # It converts the string into upper-case
print(e1)

nm = "java script"
e3 = nm.capitalize()  # It converts the first character of the string in upper-case
print(e3)

e4 = nm.title()
print(e4)          #It converts the first character of every word present in the string in upper-case.

hr = "jAVA sCRIPT"
e5 = hr.swapcase()
print(e5)             # swapcase() method swaps the lowercase into uppercase and vice-versa

