students=[[1001,'ajay','mca',150],
            [1002,'vijay','bca',145],
            [1003,'arun','mca',150],
            [1004,'amal','bca',135]]

for student in students:
    print(student[1]) #student name

for student in students:
    print(student[0]) #student roll numbers

for student in students:
    if student[2]=='mca':
        print(student) #those who study mca

for student in students:
    if student[3]>140:
        print(student)

sum_mca=0
sum_bca=0

for student in students:
    if student[2]=='mca':

        sum_mca=sum_mca+student[3]

for student in students:

    if student[2] == 'bca':
        sum_bca = sum_bca + student[3]

print('mca whole total',sum_mca)
print('bca whole total',sum_bca)

