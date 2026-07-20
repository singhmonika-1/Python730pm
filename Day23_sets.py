# Sets
#Def : A set in python is a built-in data type used to store a collection of unique elements.
#      Sets are unordered, mutable and do not allow duplicate values.
#list
l = [10,20,10]
print(l)
print(type(l))

# set
s = { 11,22,33,44}
print(s)

# set
s1 = {22,44,55,22}
print(s1)

# dictinoary
d = {"name" : "Priya"}

#tuple
t = (22,33,44,55)
print(t)
print(type(t))

# set stores unique values only
s2 = {"Pune","Mumbai","Jaipur","Agra"}
print(s2)

s3 = {"Python",22,True,33.45}
print(s3)

# set does not store value by index
# print(s3[0])

#Checking membeship of elements in sets
s4 = {100,200,300,400}
print(400 in s4)  # Boolean value(True/False)
print(301 in s4) # False

name = {"Riya", "Priya","Sheetal","Anita"}
print("riya" in name)# False

name1 = { "Riya", "Priya","riya"}
print(name1)

num = {22,44,55,44,55,66,88,11}
print(num)

# sets are mutable
num.add(56)
print(num)

name = { "Pune","Delhi","Jaipur","Kolkata"}
name.add("Nagpur")
print(name)

# update
s5 = {33,44,55,66}
s5.update([1,2,3])
print(s5)

s5.update((6,7,8))
print(s5)

#remove
s5.remove(66)
print(s5)

# s5.remove(66,44)
# print(s5) #set.remove() takes exactly one argument


# pop
s5.pop()
print(s5)


