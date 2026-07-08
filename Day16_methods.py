# String Methods

# split()
s1 = "Jaipur - Mumbai - Pune - Kolkata"
e = s1.split("-")
print(e)               # split() method split the string into list

# Replace
info1 = "I am learing Python"
e1 = info1.replace("Python","Javascript")
print(e1)

#Partition()
str2 = "a=b=c=d=e=f"
e3 = str2.partition("=")
print(e3)

u = "er-rt-ty-fgt"
e4 = u.partition("-")
print(e4)

# e5 = u.partition() TypeError: str.partition() takes exactly one argument (0 given)
# print(e5)

t1 = str2.rpartition("=")
print(t1)

# index()
st = "Bananas"
q1 = st.index("a")
print(q1)

q2 = st.index("a",2)
print(q2)

q3 = st.index("a",2,5)
print(q3)

# q4 = st.index("a",2,6)
# print(q4)

# count()

st5 = "Python Programming"
t2 = st5.count("o")
print(t2)

t3 = st5.count("p") # count() is case-sensitive
print(t3)

# join()
info = ["monikasingh","gmail.com"]
t4 = "@".join(info)
print(t4)

days = ["Monday","Tuesday","Wednesday"]
t5 = "|".join(days)
print(t5)

#find()
st7 = " apple  banana apple" # It searches the subtring from the beginning(left-side) of the string
t6 = st7.find("apple")
print(t6)

t7 = st7.rfind("apple")  # It searches from the end(right-side) of the string
print(t7)

