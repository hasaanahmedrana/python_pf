''' TYPE CASTING: change of data type from one to another. It can be done in two ways:
1- implicit (automatic)
2-  explicit (manual)
Implicit: done by python itself. For example, adding an integer and a float will result in a float.
Explicit: done by the programmer. For example, converting a string to an integer using int() function.

Few Inbuilt functions for type casting:
1- int()  # converts to integer
2- float()  # converts to float
3- str()  # converts to string
4- floor()  # rounds down the number
5- ceil()  # rounds up the number
'''

# Implicit Type Casting
num1 = 10
num2 = 10.5
result = num1 + num2
print(result)
print(type(result))
print('-' * 20)

# Explicit Type Casting
num3 = 20
num4 = '10'
result = num3 + int(num4)
print(result)
print(type(result))
print('-' * 20)


'''
IDENTITY OPERATORS: 'is and  is not (checks if two variables are pointing to the same memory location)'
Membership Operators: in and not in (checks if a value is present in a sequence or not)


Differ bw == and is operators: (== checks if the values are equal, is checks if the memory location is same)
id() function: returns the memory location of a variable

Example:
'''
num1 = 1
num2 = 10
print(num1 == num2)  # True
print(num1 is num2)  # True (only in numbers case else False you can see that in next example)
print(id(num1))  # memory location of num1 and num2 will be same
print(id(num2))



lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False
print(id(lst1))  # memory location of lst1 and lst2 will be different
print(id(lst2))


# Membership Operators
print(1 in lst1)  # True
print(1 not in lst1)  # False
print(4 in lst1)  # False
print(4 not in lst1)  # True
print('-' * 20)



