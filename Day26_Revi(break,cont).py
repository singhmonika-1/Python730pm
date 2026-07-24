#for
for x in range(1,5):
    print(x)

for x in range(5,51,5):
    print(x)    

for x in range(90,8,-9):
    print(x)  

# while
i1 = 0
while i1<6:
    print(i1) 
    i1 =i1+1     

i2 = 6
while i2 <61:
    print(i2)
    i2 = i2 +6

# Break : break statement is used to terminate the loop

for x in range(1,9):
    print(x)
    if (x == 5):
        break    #1  2  3  4 5

for x in range(1,10):
    if (x == 4):
        break
    print(x)    #1  2  3  


# continue : The continue statement is used inside loops to skip the current iteration and jump to the next iteration of the loop
# iteration -- one cycle of loop
for x in range(3,9):
    if (x == 6):
        continue
    print(x)  # 3  4  5 7 8

for x in range(8,1,-1):
    if ( x == 5):
        continue
    print(x)    


    
