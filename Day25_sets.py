# set methods
#union
s1 = {10,20,30,40}
s2 = {40,30,80,90}
r1 = s1.union(s2) 
print(r1)   #{40, 10, 80, 20, 90, 30}

#intersection
r2 = s1.intersection(s2)
print(r2)              #{40, 30}

#intersection_update
t1 = s1.intersection_update(s2)
print(t1)   # None
print(s1) #{40, 30}
print(s2)  #{40, 90, 80, 30}

# difference
s4 = {2,3,4,9}
s5 = {6,7,8,9}
r5 = s4.difference(s5)
print(r5) #{2, 3, 4}
r6 = s5.difference(s4)
print(r6)  #{8, 6, 7}

#difference_update
s6 = {10,20,30,40}
s7 = {30,70,80,90}
t5 = s6.difference_update(s7)
print(t5) #None
print(s6)        # {40, 10, 20}
print(s7)         #{80, 90, 70, 30}

#symmetric_difference   # symmetric_difference returns a new set and removes the common elements which are present in both the sets.
s8 = {11,22,33,44}
s9 = {44,55,66,22}
t7 = s8.symmetric_difference(s9)
print(t7)  # {33, 66, 11, 55}
print(s8)#{33, 11, 44, 22}

# symmetric_difference_update
s8.symmetric_difference_update(s9)
print(s8)#{33, 66, 11, 55}

#issubset
setA = {11,22}
setB = {11,22,33}
print(setA.issubset(setB)) #True
print(setB.issubset(setA))  #False

#isdisjoint
setL = {11,44}
setM = {11,22,33}
print(setL.isdisjoint(setM))  #False

setC = {10,20,30}
setD = {50,60,70}
print(setC.isdisjoint(setD)) # True

# isdisjoint(): It returns True value if there is no common element in both the sets but if there is common element then it returns False.

setX = {4,5,6}
setY = setX.copy()
setX.remove(4)
print(setX)#{5, 6}
print(setY)

