'''Dictionary
->  In real world Problems, mostly data exist in key value pair.
    For Example: User's username and password or Student's roll number or grade.
    Using simple list or other methods, searching lead to time complexity error.
    For avoiding Time complexity in searching, a data structure called hash table is the best. It return value in constant time.
    Each  hash table have a hash function for each key provide with a unique index. But guess what in python;
    you don't need to implement this , an already implemented hash table called dictionary is available to use.
    Dictionary store data in the form of key value pair seperated by colon like
    grades = { '1': A+, '2': C, '3': B-}
    All key values pair are seperated by comma.
    You can add new pair in dictionary by this syntax:
        dictionary[key] =  value

'''

users = {'musaab': 1234, 'faisal': 5678, 'mumoon': 91011}

def check_unique_username(usr):
    if usr in users:
        return False
    return True

def user_info_intake():
    while True:
        username = input('Enter your username to set: ')
        if check_unique_username(username):
            break
    password = input('Enter Password: ')
    users[username] = password


print(users)
user_info_intake()
print(users)