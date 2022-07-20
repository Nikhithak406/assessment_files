print("Enter the names as comma seperated")
t_string = input()
t_list=t_string.split(',')
vals = set(t_list[0]).intersection(t_list[1])
t = dict.fromkeys(map(ord,vals), None)
final_str=f'{t_list[0].translate(t)}{t_list[1].translate(t)}'
print(final_str)