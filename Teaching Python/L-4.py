'''
Tuples:
    - Tuples are immutable
    - Tuples are ordered
    - Tuples are represented by ()
    - Tuples support indexing and slicing
    - Tuples support concatenation and replication
    - Tuples can store duplicate items
    - Tuples can store different data types (heterogeneous)
    - Tuples can store nested tuples
    - Changes can be made
'''


# creation
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))
print('-' * 20)

# indexing
print(t[0])
print(t[1])
print('-' * 20)

# slicing
print(t[0:2])
print('-' * 20)

# concatenation
t2 = (6, 7, 8)
print(t + t2)
print('-' * 20)

# replication
print(t * 2)
print('-' * 20)

# changing the value of an item
# Uncomment the line below to see the error: (Tuples are immutable)
# t[0] = 10  # Error
print('-' * 20)


# Packing and Unpacking in Tuples
# Packing
a = 1
b = 2
c = 3
t2 = (a, b, c)
print(t2)

# Unpacking
x, y, z = t2
print(x)
print('-' * 20)





