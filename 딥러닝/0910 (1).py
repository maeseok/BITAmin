import numpy as np

np.random.seed(42)
# Hw1-1
a = np.random.randint(0,11,size=(36,))
print(a)

# Hw1-2
a = a.reshape(2,3,6)
print(a)

# Hw1-4
b = a.reshape(4,9)
print(b)
print()

# Hw1-5
c = (b+4).T
print(c)

# Hw1-6
d = b@c
print(d)

# Hw1-7
e = np.array([
    [b[0, 0], b[0, 2], b[0, 4], b[0, 6]],
    [b[1, 1], b[1, 3], b[1, 5], b[1, 7]],
    [b[2, 0], b[2, 2], b[2, 4], b[2, 6]],
    [b[3, 1], b[3, 3], b[3, 5], b[3, 7]]
])
print(e)