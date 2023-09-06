
x="AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design."


#TASK-1
spaces=0
for i in range (len(x)):
    if x[i]==' ':
        spaces+=1
print('Total Words:',spaces+1)
char=65
sum=0
for i in range (26):
    count_char=0
    if ord(x[0])==char or ord(x[0])==char+32:
        count_char+=1
        sum+=1
    for j in range (len(x)):
        if (x[j]==' '):
            if ord(x[j+1])==char or ord(x[j+1])==char+32:
                count_char+=1
                sum+=1
    if count_char>0:
        print(f'Words start with {chr(char)} appears {count_char} times in paragraph')
    char+=1
print("Total words by counting words of individual alphabets",sum)


#TASK-2
char=65
count_char=0
for i in range (26):
    for j in range (len(x)):
        if (ord(x[j])==char) or  (ord(x[j])==char+32):
            count_char+=1
    print(f'Letter {chr(char)} appears {count_char} times in paragraph')
    char+=1
    count_char=0
for i in range (len(x)):
    if x[i]==',' or x[i]==' ' or x[i]=='.':
        count_char+=1
print('Total alphabets in paragraph:',len(x)-count_char)
print('Total characters in paragraph:',len(x))