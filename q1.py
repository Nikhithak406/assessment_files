import math
print("Enter the number of rounds")
rounds = int(input())
diameter =7
rad = diameter/2
circumference = 2*math.pi*rad
total_km = circumference*rounds
print(f'{total_km} Kms travelled')
