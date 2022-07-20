from itertools import permutations
print('Enter the array')
arr = [int(x) for x in input().split()]
print('Enter the expected sum')
n = int(input())
ls=[]
perm = permutations(arr, 2)
for i in list(perm):
    if n == sum(i):
        tmp=list(i)
        ls.append(sorted(tmp))
if len(ls)>1:
    tmp_ls=[]
    for item in ls:
        if item not in tmp_ls:
            tmp_ls.append(item)
    for i in tmp_ls:
        print(i,end=' ')
else:
    for i in ls:
        print(i,end=' ')
        