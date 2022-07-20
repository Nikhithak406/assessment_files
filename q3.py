import string, random

r_letter = random.choice(string.ascii_letters)
print('Enter text')
txt = input()
r_txt = txt[::-1]
enc_string=r_letter+r_txt
print(enc_string)