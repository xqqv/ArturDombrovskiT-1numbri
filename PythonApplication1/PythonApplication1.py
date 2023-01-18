#1
n = int(input("Sisestage arv vahemikus 1 kuni 9: "))

puu = '   /V\\    '

for i in range(n):
    print(puu)
    if i<n-1:
        print(' '*(len(puu)-4) + '/ V \\  ')
        print(' '*(len(puu)-4) + '/ V V \\ ')
        print(' '*(len(puu)-4) + '/VV V VV\\')

#2
r = int(input("Sisestage number: "))
result = 1
for i in range(0, r+1):
    if i % 2 != 0:
        result *= i
print(result)

#3
import random

n = int(input("Sisestage number: "))
positive_count = 0

for i in range(n):
    num = random.randint(-100, 100)
    if num > 0:
        positive_count += 1

print("Positiivsete arvude arv: ", positive_count)

#4 
num = int(input("Positiivsete arvude arv: "))
even_count = 0
odd_count = 0

while num > 0:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10

print("Isegi loe: ", even_count)
print("Paaritu arv: ", odd_count)

