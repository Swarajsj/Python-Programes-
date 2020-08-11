# Program to print the Armstrong number

num = int(input('Enter values'))
sum = 0
x = num
while num > 0:
    d = num % 10
    num = num // 10
    sum = sum + (d*d*d)
if x == sum:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')
