from itertools import permutations
import random
print('Enter subjects seperated by commas')
t_list = input().split(',')
vals = []
t_table=[]
for items in permutations(t_list):
    vals.append(list(items))
sub1=[]
sub2=[]
sub3=[]
sub4=[]
sub5=[]
sub_list=[sub1,sub2,sub3,sub4,sub5]
for item in vals:
    if item[0]==t_list[0]:
        sub1.append(item)
    elif item[0]==t_list[1]:
        sub2.append(item)
    elif item[0]==t_list[2]:
        sub3.append(item)
    elif item[0]==t_list[3]:
        sub4.append(item)
    elif item[0]==t_list[4]:
        sub5.append(item)
for i in sub_list:
    t_table.append(random.choice(i))
counter=1
for item in t_table:
    
    print(f'Day {counter} Timetebale',end="\n")
    for element in item:
        print(f'{element}',end=" ")
    counter+=1
    print()
