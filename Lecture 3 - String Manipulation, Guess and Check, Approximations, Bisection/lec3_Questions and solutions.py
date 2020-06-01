# 1 - String Manipulations
# What does the code below print?

s = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s[-1]
new_str += s[0]
new_str += s[4::30]
new_str += s[13:10:-1]
print(new_str)

# 26 100


# 2 - For Loops with Strings
# How many times will the code below print "common letter"?

s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break

# 7
