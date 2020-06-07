# 1 - Getters and Setters

# Which of the below is a getter method for the number of wheels?

----------------------------------
----------- Given ------------
----------------------------------
class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""
----------------------------------

(A)    def get_wheels():
             return wheels

(B)    def get_wheels():
             return self.wheels

(C)    def get_wheels(self):
             return wheels

(D)    def get_wheels(self):
             return self.wheels

#  def get_wheels(self):
      return self.wheels


# 2- Subclass

# Whate line could replace ____blank____ to create a class that inherets from Animal in the code below?

____blank____
    def speak(self):
        print("ruff ruff")

(line1) d = Dog(7)
(line2) d.set_name("Ruffles")
(line3) d.speak()

# class Dog(Animal):

# With this definition of Dog, you run a program with line1, line2, and line3 above. What happens? Refer to the lecture slides for the code making up the "Animal" class.

# Runs, creates a Dog object with age=7 and name="Ruffles", and prints "ruff ruff"