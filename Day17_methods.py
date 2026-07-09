#index() method
st = "Banana"

# B  A  N  A  N  A
# 0  1  2  3  4  5
e = st.index("a",1)
print(e)

e1 = st.index("a",2,5)
print(e1)

e2 = st.index("a",4,6)
print(e2)

# strip
info = "   Rao "
t = info.strip()
print(t)     # strip() method removes both sides(leading and trailing) spaces.

info1 = "    Hello"
t1 = info1.lstrip() # lstrip() method removes left(leading ) spaces only.
print(t1)

info3 = " Hi     "
t2 = info3.rstrip() #rstrip() method removes right(trailing) spaces only
print(t2)


# String Concatenation
print("Hello World")
print("Hello"+ " "+ "World") # the + operator joins strings together. This process is called as string concatenation.

FirstName = "Monika"
LastName = "Singh"
print("I am"+" "+ FirstName +" "+LastName)

print("I am",FirstName,LastName) #print() with commas atutomatically inserts a single space between each argument.

print(f"I am {FirstName}       {LastName}") #This "f" is called as f-string(formatted string literal). This is used to combine string and variables.


# Dictionary
l = ["Sarita",22,"Pune","51"]#list

#         Key            value
info = {"First Name" : "Sarita",
        "Last Name": "Rao",
        "Age" : 22,
        "City" : "Pune"}
print(info)
