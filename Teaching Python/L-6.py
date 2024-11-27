'''
ASCII CONVERSIONS FUNCTIONS:
    ord() - converts a character to its ASCII value
    chr() - converts an ASCII value to its character

Tips for Patterns:
1 - Observe the pattern carefully
2 - Try to find the relation between the numbers
3 - Try to find the relation between the rows
4 - Try to find the relation between the columns
Mostly outer loop is for rows(lines) and inner loop is for columns(elements in each inner loop)
'''

# ord() function
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('0'))  # 48

# chr() function
print(chr(65))  # A
print(chr(97))  # a
print(chr(48))  # 0
print('-' * 20)


'''
TRY THE FOLLOWING PATTERNS:

FIRST:
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5

SECOND:
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
F F F F F


THIRD:
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9


FOURTH:
1 
 2
  3
   4
    5

FIFTH:
A B C D E
B C D E F
C D E F G
D E F G H
E F G H I


SIXTH:
1
1*2
1**2**3
1***2***3***4
1****2****3****4****5


SEVENTH:
----5
---4
--3
-2
1


EIGHTH:
Take user inputs number of rows(n)and columns(m) and print n*m matrix.
For example user added 3 and 4 then print 3*4 matrix.
****
****
****
'''