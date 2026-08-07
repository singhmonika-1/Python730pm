# Decorator

def my_dec(fun):
    def inner(a,b):
        print(f"Adding {a} and {b}")
        result = fun(a,b)
        print(f"Addition = {result}")
    return inner

@my_dec
def addition(a,b):
    return a+b

addition(5,6)    


def positive(fun):
    def inner(num):
        if num > 0 :
            fun(num)
        else:
            print("Plese enter a positive number") 
    return inner

@positive
def sq(num):
    print(num * num)

sq(3) 
sq(-6) 
sq(10)  

def decorOne(fun):
    def inner():
        val  = fun()
        return val+2
    return inner

def decortwo(fun):
    def inner():
        val = fun()
        return val*10
    return inner

@decorOne
@decortwo
def call():
    return 10

e = call()
print(e)

# Exception handling

# write program -------compile ------ run-----output

# 1.compile time error/Syntax error
# 2. run time error
# 3.logical error

#compile time errors are syntax error
print("Hello)


    


                 