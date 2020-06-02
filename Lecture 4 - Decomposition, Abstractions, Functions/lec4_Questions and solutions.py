# 1 - Function Calls
# How many total lines of output will show up if you run the code below?
def add(x, y):
    return x + y


def mult(x, y):
    print(x * y)


add(1, 2)
print(add(2, 3))
mult(3, 4)
print(mult(4, 5))

# 4


# 2 - Functions as Arguments

# What does the code below print?


def sq(func, x):
    y = x ** 2
    return func(y)


def f(x):
    return x ** 2


calc = sq(f, 2)
print(calc)

# 16
