# 1 - Black Box and Glass Box Testing

# With the below implementation, is the test set "n = 4 | n = -4 | n = 5" path complete?

def is_even(n):
    """
    Returns True if a number is even
    and False if not
    """
    if n > 0 and n % 2 == 0:
        return True
    elif n < 0 and n % 2 == 0:
        return True
    else:
        return False

# Yes

# With the above implementation, which value for n is incorrectly labeled by is_even?
    # n is 0


# 2 - Errors

# Below is a piece of code and an error shown when running it. What is the problem?

L = 3
for i in range(len(L)):
    print(i)

ERROR MESSAGE:

 File "C:/Users/Ana/.spyder2-py3/temp.py", line 2, in
    for i in range(len(L)):

TypeError: object of type 'int' has no len()

# You are not allowed to call len on an integer


# 3 - Exceptions
# If the user enters "twenty" in the code below what does the program do?

try:
    n = int(input("How old are you? "))
    percent = round(n*100/80, 1)
    print("You've gone through", percent, "% of your life!")
except ValueError:
    print("Oops, must enter a number.")
except ZeroDivisionError:
    print("Division by zero.")
except:
    print("Something went very wrong.")

# prints "Oops, must enter a number."

# If the user enters "0" in the code above what does the program do?

# prints "You've gone through 0.0 % of your life!"
