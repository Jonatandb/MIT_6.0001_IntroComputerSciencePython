from numpy import log2

fNumber = input("Enter a number:")
sNumber = input("Enter a second number:")
print(str(fNumber) + "**" + str(sNumber), "=", int(fNumber) ** int(sNumber))
log = log2([int(fNumber)])
print("log(" + fNumber + ") =", str(int(log)))
