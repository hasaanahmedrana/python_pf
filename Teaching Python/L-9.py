'''
To be Discussed in this class:

Dictionary related functions:
1- update() function -(upd,add,merge)
2- clear() function vs del keyword
3- copying dictionaries
4- accessing elements in nested dictionaries

List related functions:
1- zip() function
2- enumerate() function (start)
3- map() function
4- filter() function
5`- reduce() function

Loop Control:
1- pass
2- break (in nested loops)
3- continue
4- return
5- for else / while else
'''

from copy import *
my_info = {'Name': 'Hasaan',
        'Age': 21,
        'Nationality': 'Pakistani',
        'DOB':{'date': 7,
               'month': 3,
                'year': 2003}
}

print('Before update:', my_info)
# update
# updates the value if key exists
my_info.update({'Name': ' Hasaan Ahmad'})
print('After updating Name:', my_info)

# adding new key-value pair if key doesnot exists
my_info.update({'University': 'PUCIT'})
print('After adding University:', my_info)

# merging second dictionary argument in the first one
my_education = {'Education': 'Bachelors'}
my_info.update(my_education)
print('After merging:', my_info)

print('-' * 50)

# clear() function vs del keyword
# clear() function clears the dictionary
my_info.clear()
print('After clear:', my_info) # exists but empty

# del keyword deletes the dictionary
del my_info # deletes the dictionary
#print(my_info)  will return error if uncomments as my_info doesnot exists anymore.
print('-' * 50)



my_info = {'Name': 'Hasaan',
        'Age': 21,
        'Nationality': 'Pakistani',
        'DOB':{'date': 7,
               'month': 3,
                'year': 2003}
}

# Copying dictionaries
#1- ALIASING
hasaan_info = my_info # its just aliasing; all the changes in each of them will appear in both
print(id(my_info), id(hasaan_info)) # same id means same objects


#2- SHALLOW COPY
hasaan_info = my_info.copy() # creates a new dictionary with same values
print(id(my_info), id(hasaan_info)) # different id means different objects

'''
limitation:
if there are nested dictionaries, then the nested dictionaries will be aliased  
and changes in nested dictionary will appear in both.
In the example below you can see ; changing hasaan nationality will not appear in my_info
but changing hasaan's dob' year will appear in both.
'''
hasaan_info['Nationality'] = 'Indian'
hasaan_info['DOB']['year'] = 2000
print('MY_INFO', my_info)
print('HASAAN_INFO', hasaan_info)
print('-' * 50)

#3- DEEP COPY:
# to avoid the limitation of shallow copy, we use deep copy function,
# any change in new copy will not appear in my_info and vice versa
hasaan_info = deepcopy(my_info) # creates a new dictionary with same values
print(id(my_info), id(hasaan_info)) # different id means different objects

hasaan_info['Nationality'] = 'American'
hasaan_info['DOB']['year'] = 1999
print('MY_INFO', my_info)
print('HASAAN_INFO', hasaan_info)
print('-' * 50)


# Accessing elements in nested dictionaries
print(my_info['DOB']['year'])
print(my_info['DOB']['month'])
print(my_info['DOB']['date'])
print('-' * 50)

# List related functions
# zip() function
names = ['Hasaan', 'Ali', 'Ahmad']
ages = [21, 22, 23]
for name, age in zip(names, ages):
    print(name, age)
print('-' * 50)

# enumerate() function
for index, name in enumerate(names, start=1):
    print(index, name)
print('-' * 50)


lst = list(map(int,input().split()))