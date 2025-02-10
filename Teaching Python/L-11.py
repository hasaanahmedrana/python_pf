print('----TASK-1---')
s = input()
print(s[::2])

print('----TASK-2---')
def vowelCount(string):
    count = 0
    vowels = ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U')
    for i in string:
        if i in vowels:
            count += 1
    return count

s = input()
print(vowelCount(s))

print('----TASK-3---')
def mirror(string):
    r = string[::-1]
    print('ORIGINAL',string, ',', 'REVERSED', r)

s = input()
mirror(s)

print('----TASK-4---')

def name_contain(name, letter):
    if letter in name:
        return True
    return False
name = input()
letter = input()
print(name_contain(name, letter))


# print('----TASK-5---')
def remove_char(string, idx):
    print(string[:idx] + string[idx+1:])

s = input()
idx = int(input())
remove_char(s,idx)

print('----TASK-6---')
def remove_elem(string, char):
    # STRINGNAME.REPLACE('CHARACTER TO BE REPLACED, NEW CHARACTER, COUNT))
    new_string = string.replace(char, '')
    print(new_string)
s = input()
char = input()
remove_elem(s, char)

