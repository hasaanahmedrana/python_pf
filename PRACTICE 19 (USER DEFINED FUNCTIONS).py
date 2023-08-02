c#  #TASK(a)
# def print_50_eveninteger(a,b):
#     i=a
#     count=1
#     while count<=b:
#         print(i)
#         count+=1
#         i+=2
#     return
# start_num=int(input('Number to start from :'))
# if start_num%2 !=0:
#     start_num+=1
# n_times=int(input('Number of even numbers to be printed:'))
# a=print_50_eveninteger(start_num,n_times)


# #TASK(b)
# #function to print character c, n times
# def character_c_n_times(c,n):
#     i=1
#     while i <= n:
#         print(c)
#         i+=1
#     return
# charac=input('Character to be prointed:')
# n_times=int(input('Number of times to be printed:'))
# a= character_c_n_times(charac,n_times)

# #TASK(c)
# #counting first n integers with distance d
# def n_int_with_distance_d(n,d):
#     count=1
#     i=1
#     while count<=n:
#         print(i)
#         i+= d
#         count+=1
#     return
# n=int(input('Number of integers to be printed:'))
# d=int(input('Distance between integers:'))
# a=n_int_with_distance_d (n,d)

# #TASK(D)
# #sum of first n integers
# def sum_n_int(n):
#     i=1
#     count=1
#     sum=0
#     while count<=n:
#         sum+=i
#         i+=1
#         count+=1
#     return sum
# n=int(input('To find sum upto :'))
# print('sum:',(sum_n_int(n)))
#TASK(e)
#to find next vowel
def fiind_next_vowel(n):
    a=ord(n)
    if a<69:
        nextvowel='E'
    elif a<73:
        nextvowel='I'
    elif a<79:
        nextvowel='O'
    elif a<85:
        nextvowel='U'
    elif a<101:
        nextvowel='e'
    elif a<105:
        nextvowel='i'
    elif a<111:
        nextvowel='o'
    elif a<117:
        nextvowel='u'
    return nextvowel
n=input('Enter Character:')
print('Next vowel is :',fiind_next_vowel(n))


