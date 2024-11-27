'''
Dictionary:
-> ordered collection of items(key-value pair)
-> constant time data retrieval or searching. (hash table) - O(1) time complexity
-> elements or items are seperated by comma, key value seperated by colon.
-> key has to be immutable.(cant be list or dictionary)
-> value can be of any data type.(list, dictionary, tuple, set, string, integer, float)
'''

english_marks = {
                'Ali': 90,
                 'Ahmad': 80,
                 'Musaab': 70,
                 'Imran': 34,
                 'Mamoon': 73
                 }

# Accessing elements in a dictionary
print('---ACCESSING ELEMENTS---')
# Method-1  This method will return error if key does not exist in the dictionary.
print(english_marks['Ali'])
print(english_marks['Ahmed'])

# Method-2  # This method will return "None" if key does not exist in the dictionary.
print(english_marks.get('Ali'))
print(english_marks.get('Ahmed'))

'''Imagine the upper scenerio, hasaan failed to attempt english exam, so his name is not in the dictionary.
If we use method-1, it will return error, but if we use method-2, it will return None.
But logically returning None to marks is not correct we should return 0, 
so by using method 2 we can value which will be return if key doesnot exists.'''

print(english_marks.get('Hassan', 0))

print('-' * 20)

# Changing the value of an item
print('---CHANGING VALUE---')
english_marks['Ali'] = 95
print(english_marks) # you can see the value of Ali is updated.

# Adding a new item
english_marks['Saleh'] = 0
print(english_marks) # you can see the new item is added.

# Deleting an item
'''
3 ways:
dictionay.pop(key)  # delete same key pair and returns the value of the key
del dictionary[key]  # delete same key pair and returns nothing
dictionary.popitem()  #  delete the last key pair and returns the last item
'''
print('---DELETING ITEM---')


del english_marks['Saleh']
print(english_marks) # you can see the new item is deleted.
print(english_marks)
print(english_marks.pop('Mamoon')) # you can see the value of Mamoon is deleted.
print(english_marks)
print(english_marks.popitem()) # you can see the last item is deleted.


# Dictionary Methods
# 1- keys()  # returns all the keys in the dictionary
# 2- values()  # returns all the values in the dictionary
# 3- items()  # returns all the key-value pairs in the dictionary

print('---DICTIONARY METHODS of ACCESS---')
for i in english_marks.keys():
    print(i)
print('-' * 20)

for i in english_marks.values():
    print(i)
print('-' * 20)

for i,j in english_marks.items():
    print(i,':',j)
print('-' * 20)


# other wayt of accessing keys, values
for i in english_marks:
    print(i, ':', english_marks[i])
print('-' * 20)


# sorting dictionary
# sorted() function takes 3 arguments
# 1- dictionary name
# 2- key(optional) # takes a function as argument
# 3- reverse(optional) # True or False

print('----SORTING----')
# sorting by keys (no key argument will sort based upon key
sorted_dict = sorted(english_marks.items())
print(sorted_dict)
print('-' * 20)


# sorting by values (key argument will sort based upon value)
sorted_dict = sorted(english_marks.items(), key=lambda x: x[1])
print(sorted_dict)
print('-' * 20)


# sorting by values in reverse order
sorted_dict = sorted(english_marks.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)
print('-' * 20)



print('---Clearing Dictionary------')
english_marks.clear()
print(english_marks)  # you can see the dictionary is empty now.
