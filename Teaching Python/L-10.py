# REPLACING ELEMENTS OF STRING BY INDEXES
print('-----METHOD - 1: USING SLICING-----')
s = input()
idx1 = int(input())
idx2 = int(input())
# make sure idx1 is less than idx2 else replace their value
if idx1 > idx2:
    idx1, idx2 = idx2, idx1
# replace the elements using slicing
s = s[:idx1] + s[idx2] + s[idx1+1:idx2] + s[idx1] + s[idx2+1:]
print(s)
'''
let suppose s = 'HASAANRANA'
idx1 = 2
idx2 = 5
s[idx1] = 'S' and s[idx2] = 'N'
s[0:idx1] = 'HA' + s[idx2] = 'N' + s[idx1+1:idx2] = 'AA' + s[idx1] = 'S' + s[idx2+1:] = 'RANA'
'HA' + 'N' + 'AA' + 'S' + 'RANA' = 'HANAASRANA'
'''

print('-----METHOD - 2: USING FOR LOOP-----')
s = input()
idx1 = int(input())
idx2 = int(input())
new_s = ''
for i in range(len(s)):
    if i == idx1:
        new_s += s[idx2]
    elif i == idx2:
        new_s += s[idx1]
    else:
        new_s += s[i]
print(new_s)

print('-----METHOD - 3: ----')
s = input()
idx1 = int(input())
idx2 = int(input())
s[idx1], s[idx2] = s[idx2], s[idx1]
print(s)


