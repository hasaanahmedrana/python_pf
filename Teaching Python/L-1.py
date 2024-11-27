myName1 = 'mumoon faisal'
# triple quotes string can extend multiple lines.
myName2 = '''mumoon
faisal'''
print(myName1)
print(len(myName1))
print('-' * 20)  # printing line using string repetition.

print(myName2)
print(len(myName2))
print('-' * 20)



print('---INDEXING---')
# Accessing characters in a string.(CONCEPT OF INDEXING)
print(myName1[0])
print(myName1[1])
print(myName1[2])
print(myName1[-1])  # last character
print(myName1[-2]) # second last character
print(myName1[-3]) # third last character



print('---SLICING---')
# Accessing characters in a string.(CONCEPT OF SLICING)
# Syntax: stringName[start:stop:step]  # stop is not included. (stop -1 is the last character)
print(myName1[0:2])  # 0 to 2
print(myName1[2:5])  # 2 to 5
print(myName1[2:])  # 2 to end
print(myName1[:5])  # start to 5
print(myName1[:])  # whole string
print(myName1[::2])  # every second character
print(myName1[::-1])  # reverse the string
print(myName1[::-2])  # reverse the string with every second character
print(myName1[5:2:-1])  # 5 to 2 in reverse order
print('-' * 20)


print('---IMMUTABILITY---')
# Strings are immutable. (Cannot change the value of a string) important point
# Uncomment the lines below to see the error:

# myName1[0] = 'M'  # Error
# myName1[0:2] = 'Mu'  # Error
print('-' * 20)



print('---STRING CONCATENATION---')
# Concatenating strings (joining strings using + operator)
print(myName1 + myName2)
print(myName1 + ' ' + myName2)
print('-' * 20)


print('---STRING REPLICATION---')
# Replicating strings (repeating strings using * operator)
print(myName1 * 2)
print('-' * 20)


print('---STRING METHODS---')
# Some useful string methods. 1- upper(), 2- lower(), 3- capitalize()

print(myName1.upper())
print(myName1.lower())
print(myName1.capitalize())



'''VARIABLE NAMING CONVENTIONS:
1- Camel Case: myNameIsMumoon
2- Pascal Case: MyNameIsMumoon
3- Snake Case: my_name_is_mumoon


-> Variable name is case sensitive.
-> Variable name cannot start with a number.
-> Variable name can contain letters, numbers and underscore.
-> Variable name cannot contain special characters.
-> Variable name should be meaningful.
'''

MyRollNumber = 1234 # Pascal Case
my_roll_number = 1234 # Snake Case
myRollNumber1 = 1234 # Camel Case

print('-' * 20)

