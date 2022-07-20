def count_char(t_string):
    tmp_ls=[]
    counter=0
    letter_set=[]
    for i in range(0,len(t_string)):
        if t_string[i] not in letter_set:
            letter_set.append(t_string[i])
    for item in letter_set:
        counter=0
        for i in t_string:
            if i ==item:
                counter+=1
        if counter==1:
            tmp_ls.append(item)
        else:
            tmp_ls.append(f'{item}{counter}')
    return ''.join(tmp_ls)

print('Enter String')
inp_str = input()
ls=[]
word_list = inp_str.split(' ')
for item in word_list:
    ls.append(count_char(item))
print(' '.join(ls))
