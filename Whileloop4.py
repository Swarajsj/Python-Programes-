# Programs to disolay the reverse of numbers

num = int(input('Enter the value'))
r = 0
while num > 0:
    p = num % 10
    num = num // 10
    r = r*10+p
print(r)
