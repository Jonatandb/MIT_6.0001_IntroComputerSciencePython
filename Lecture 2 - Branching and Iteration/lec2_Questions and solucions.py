# 1 - Strings

# What is the value of variable `u` from the code below?

once = "umbr"
repeat = "ella"
u = once + (repeat + " ") * 4

# umbrella ella ella ella


# 2 - Comparisons

# What does the code below print?

pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)

# False False


# 3 - Branching

# What's printed when x = 0 and y = 5?

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    if y != 0:
        print("x / y is", x / y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")

# "x is smaller"


# 4 - While Loops

# In the code below from Lecture 2, what is printed when you type "Right"?

n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")

# "You got out of the Lost Forest!"


# 5 - For Loops

# What is printed when the below code is run?

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)

# 5
