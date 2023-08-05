#TASK-1
#FIND MAX AVERAGE IN CLASS AND TELL WHICH CLASS HAS MAXIMUM...
file=open('marks.txt','r')
classes_num=int(file.readline())
max_average=0
for i in range(1,classes_num+1):
    student_num=int(file.readline())
    sum=0
    for j in range (1,student_num+1):
        marks=int(file.readline())
        sum+=marks
    average=sum/student_num
    print(average)
    if max_average<average:
        max_average=average
        class_1=(f'{i}')
print(f'Maximum average is:{max_average:<2.2f} of class:{class_1}')
file.close()

#TASK-2
#PRINT MARKS OF EACH CLASS IN EACH LINE IN marks_1
file=open('marks.txt','r')
file2=open('marks_1.txt','w')
classes_num=int(file.readline())
file2.write(str(classes_num))
file2.write('\n')
for i in range(1,classes_num+1):
    student_num=int(file.readline())
    file2.write(str(student_num))
    file2.write('\n')
    for j in range (1,student_num+1):
        marks=int(file.readline())
        file2.write(str(marks)+'  ')
    file2.write('\n')

file2.write('\n')
file.close()
# file2.close()

# #TASK-3
# #create a file similar to marks.txt. The file should contain marks of 5 classes. Each class has marks of 7 to 10 students and each student has marks 0-100 at random.
from random import*
file=open('marks_create.txt','w')
class_no=5
for i in range(1,class_no+1):
    file.write((str(i))+'\n')
    student_no=randint(7,10)
    file.write((str(student_no))+'\n')
    for j in range (student_no):

        marks=randint(0,100)
        file.write((str(marks))+'\n')
    file.write('\n')
file.close()
#or(chatgpt)
from random import randint
with open('markss.txt', 'w') as file:
    class_no = 5
    for i in range(class_no):
        file.write(str(i) + '\n')
        student_no = randint(7, 10)
        file.write(str(student_no) + '\n')
        for j in range(student_no):
            marks = randint(0, 100)
            file.write(str(marks) + '\n')
        file.write('\n')

#TASK-4
#create a file matrix.txt. Generate random number for rows (4-8) and columns (4-8) Write rows and columns on the top of the file, each in single line. Next in rows * columns lines, write random elements of the matrix in range 1 to 9
from random import*
row=randint(4,8)
coloumn=randint(4,8)
file=open('matrix.txt','w')
file.write(str(row)+'\n')
file.write(str(coloumn)+'\n')
row_col=row*coloumn
for i in range(row):
    for j in range(coloumn):
        file.write(str(randint(1,9))+' ')
    file.write('\n')
file.close()
