# def gg():
#     global x
#     x = 1000

# gg()

# def hh():
#     print(x)

# hh()

# #LEARNING NONLOCAL KEYWORD
# def myfunc1():
#     x = "fantastic"
#     def myfunc2():
#         nonlocal x #The nonlocal keyword makes the variable accessible to the first function.
#         x = "awesome"
#     myfunc2()
#     return x

# print(myfunc1())



# import datetime
#                # CLASS.METHOD
# dt = datetime.datetime.now()
# print(f"Today's date is {dt}")



# # SPECIFICALLY GETTING THE YEAR, MONTH AND DAY FROM DATETIME
import datetime

dt = datetime.datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.strftime("%A"))


import math

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# x = abs(-7.25)
# print(x)

# x = pow(4,3)
# print(x)

# x = math.sqrt(64)
# print(x)

# x = math.ceil(2.5) #ROUNDS THE NUMBER UPWARDS TO ITS NEAREST INTEGER
# y = math.floor(2.5) #ROUNDS THE NUMBER DOWNWARDS TO ITS NEAREST INTEGER

# print(x, y)

import json
# import pythonn
