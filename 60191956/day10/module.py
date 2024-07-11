# 표준모듈 사용

import random
import math
import calendar

def roll_dice():
    return random.randint(1,6)
print(roll_dice())
print(roll_dice())
print(roll_dice())
print(roll_dice())

cal = calendar.month(2024, 7)
print(cal)

from calendar import *
cal = month(2024, 7)
print(cal)

import calendar as cl
cal = cl.month(2024, 7)
print(cal)

from calendar import month as mo
