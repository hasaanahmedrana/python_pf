'''
RAMDOM MODULE:

    Ways of importing random module:
        1. import random
        2. from random import *
        3. from random import randint, randrange (importing specific functions)

    Note: Import Modules in the beginning of the file.

    Some important functions of random module:
        1. random() : It returns a random floating point number in the range [0.0, 1.0).
        2. randint() : It returns a random integer number in the range [a, b].
        3- randrange() : It returns a random integer number in the range [a, b) with a step value of c.
        4- choice() : It returns a random element from the non-empty sequence.
        5- choices() : It returns a list of random elements from the non-empty sequence.
        6. shuffle() : It shuffles the elements of the non-empty sequence in place.
'''

import random
# from random import *
# Random function
x = random()  # 0.0 <= x < 1.0
print(x)
print('-' * 20)

# randint function
y = random.randint(1, 10)  # 1 <= y <= 10
print(y)
print('-' * 20)

# randrange function
z = random.randrange(1, 10)  # 1 <= z < 10
print(z)
print('-' * 20)

# choice function
lst = [1, 2, 3, 4, 5]
a = choice(lst)
print(a)
print('-' * 20)

# choices function
b = random.choices(lst, k=3) # k is the number of elements to be selected
print(b)
print('-' * 20)

# shuffle function
random.shuffle(lst) # shuffles the list in place
print(lst)
print('-' * 20)

