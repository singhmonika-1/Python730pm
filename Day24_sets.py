# sets
s1 = { 20,30,40,50}
print(type(s1))

#add
s1.add(100)
print(s1)

#update
s1.update([4,5,6])
print(s1)

# remove
s1.remove(50)
print(s1)

#pop
s1.pop()
print(s1)

#clear
s1.clear()
print(s1)  # It will print empty set
            #output : set()

# w = { 1,2,3,4}
# print(w)            
# del w
# print(w)

#loop
r1 = {10,20,30,40}
for x in r1:
    print(x)

# union
s2 = {11,22,33,44}
s3 = {44,55,66}
r2 = s2.union(s3)    # union() : It returns a new set containing all distinct(unique) elements present in the given set.
print(r2)   #{33, 66, 22, 55, 11, 44}
print(s2)
print(s3)

# intersection
r4 = s2.intersection(s3) # intersection() : it returns a new set containing only the elements that are present in both the sets.
print(r4)   #{44}

t1 = {1,2,3}
t2 = {7,8,9}
y = t1.intersection(t2) 
print(y)# set()

# intersection_update
h1 = { 11,22,33,44,55}
h2 = {44,55,88,99}
f = h1.intersection_update(h2)
print(f)  # None
print(h1)  #{44, 55}
print(h2)  #{88, 99, 44, 55}

# difference
s4 = { 10,20,30}
s5 = {30,40,50,60}
t4 = s4.difference(s5) # difference is a set operation. It returns the element present in the first set but not present in the second set.
print(t4)  # {10,20}

t5 = s5.difference(s4)
print(t5)# {40, 50, 60}






