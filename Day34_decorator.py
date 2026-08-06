# decorator
# A decorator is a function that modifies the behaviour of another function without changing its actual code.

def dec1(fun):
    def inner():
        print("Before calling the function")
        fun()
        print("After calling the function")
    return inner

@dec1
def hello():
    print("Hello Students")

hello()


def dec2(fun):
    def inner():
        e = fun()
        return "Hello" +" "+ e
    return inner

@dec2
def greet():
    return "Students"
e1 = greet()
print(e1)


def dec3(fun):
    def inner():
        result = fun()
        return result.upper()
    return inner

@dec3
def city():
    return "pune"

print(city())


def add_tax(fun):
    def inner():
        amount = fun()
        return amount + 50
    return inner

@add_tax
def bill():
    return 500

print(bill())
        