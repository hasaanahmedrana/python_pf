'''
Immutable : Tuple, String, Number (meaning you can't change the value of any of these types)
Mutable : List, Set, Dictionary (meaning you can change the value of any of these types))

List:
1- ordered collection of items
2- mutable (can change the value of items)
3- can store duplicate items
4- can store different data types (heterogeneous)
5- represented by []
6- supports indexing and slicing
7- supports concatenation and replication

'''
# Creating a list
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))
print('-' * 20)


# Accessing elements in a list
print(lst[0])
print(lst[1])
print('-' * 20)


# Slicing
print(lst[0:2])
print('-' * 20)

# Concatenation
lst2 = [6, 7, 8]
print(lst + lst2)
print('-' * 20)

# Replication
print(lst * 2)
print('-' * 20)

# Changing the value of an item
lst[0] = 10
print(lst)
lst[0:2] = [20, 30]
print(lst)
print('-' * 20)

'''
Packing and Unpacking in Lists:
Packing: packing multiple values in a single variable
Unpacking: unpacking multiple values from a single variable
'''
# Packing
a = 1
b = 2
c = 3
lst2 = [a, b, c]
print(lst2)

# Unpacking
x, y, z = lst2
print(x)

lst2 += [4, 5, 6]
print(lst2)
print('-' * 20)

m, n, *o = lst2
print('m',m)
print('n',n)
print('o',o)
print('-' * 20)

m, *n, o = lst2
print('m',m)
print('n',n)
print('o',o)


''' ALIAS ,DEEP COPY AND SHALLOW COPY
ALIAS: Same object with multiple nicknames.Have same id in memory. Change is reflected in all the nicknames.
Shallow Copy: Copy of the object but the inner objects are still the same. 
        Have different id in memory. Change in inner object is reflected in both the objects.
        DONE BY TWO METHODS:
            1- Using copy.copy() method
            2- Using list slicing [:]
Deep Copy: Copy of the object and the inner objects are also copied. Have different id in memory.
        Change in inner object is not reflected in both the objects.
        DONE BY USING copy.deepcopy() method
        '''

# Alias
lst1 = [1, 2, 3]
lst2 = lst1
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))
lst1[0] = 10
print(lst1)
print(lst2)
print('-' * 20)


# Shallow Copy
import copy
lst1 = [1, 2, 3]
lst2 = copy.copy(lst1)
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))
lst1[0] = 10
print(lst1)
print(lst2)
print('-' * 20)


lst1 = [1,2,3 ,[4, 5, 6]]
lst2 = copy.copy(lst1)
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))
lst1[3][0] = 10
print(lst1)
print(lst2)  # change is reflected in both the lists in case of nesred list because its shallow copy.
print('-' * 20)


# Deep Copy
lst1 = [1, 2, 3, [4, 5, 6]]
lst2 = copy.deepcopy(lst1)
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))
lst1[3][0] = 10
print(lst1)
print(lst2)  # change is not reflected in both the lists in case of nesred list because its deep copy.
print('-' * 20)

'''
List Methods:
1- append()  
2- insert() 
3- extend() 
4- remove()  # take value(object) as argument and remove its first occurance
5- pop()  # removes the last element by default AND takes index as argument
6- clear()
7- index()
8- count()
9- sort()
10- reverse()
'''

'''Sorted() function: takes 3 arguments
1- lst name
2- key (optional) # takes a function as argument
3- reverse (optional) # True or False

'''

lst = [1, 2, 3, 4, 5]
lst2 = sorted(lst, reverse=True)
print(lst)
print('-' *20)

lst = ['mumoon', 'faisal', 'musaab', 'hasaanrana','ali','ejaz']
lst2 = sorted(lst)
print('-' *20)

lst3 = sorted(lst, key=len)
print(lst3)
print('-' *20)


def first(s):
    return s[0]
lst4 = sorted(lst, key=first)
print(lst4)