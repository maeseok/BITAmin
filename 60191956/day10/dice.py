from random import randint

def two_dice():
    result = 0
    for i in range(2):
        result += randint(1,6)
    print(result)

def n_rolling_dice(n):
    result = 0
    for i in range(n):
        data = randint(1,6)
        result+=data
    